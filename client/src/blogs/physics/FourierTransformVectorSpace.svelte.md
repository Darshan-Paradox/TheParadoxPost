<script>
	import Eq from "../../components/Eq.svelte";
	import Ref from "../../components/Ref.svelte";
	import Frame from "../../components/Frame.svelte";

	const path = `/blogs/physics/fourier_transform_vector_space`

	const taylor_series = "f(x) = \\sum_0^\\infty a_n\\cdot x^n";
	const taylor_coeffs = "a_n = \\cfrac{1}{n!}\\cdot\\cfrac{d^n}{dx^n}f(x)";
	const taylor_rep = "f(x) \\equiv \\left[{\\begin{array}{c} a_0 \\\\ a_1 \\\\ \\vdots \\\\ a_n \\end{array}}\\right]";
	const taylor_vector = "f(x) = \\left[{\\begin{array}{cccc} x^0 & x^1 & \\cdots & x^n \\end{array}}\\right]     \\cdot     \\left[{\\begin{array}{c} a_0 \\\\ a_1 \\\\ \\vdots \\\\ a_n \\end{array}}\\right]";
	const sin_taylor = "sin(x) = x - \\cfrac{x^3}{3!} + \\cfrac{x^5}{5!} + ... + (-1)^{2n - 1}\\cfrac{x^{2n - 1}}{(2n - 1)!}";
	const sin_coeff = "a_1 = 1, a_3 = \\cfrac{-1}{3!}, a_5 = \\cfrac{1}{5!}, a_{2n - 1} = (-1)^{2n - 1}\\cfrac{1}{(2n - 1)!}";
	const sin_apprx = "sin(x) \\approx x - \\cfrac{x^3}{3!} + \\cfrac{x^5}{5!}";
	const exp_taylor = "e^x = 1 + x + \\cfrac{x^2}{2!} + \\cfrac{x^3}{3!} + ... + \\cfrac{x^n}{n!}";
	const exp_coeff = "a_0 = 1, a_1 = 1, a_2 = \\cfrac{1}{2!}, a_3 = \\cfrac{1}{3!}, a_{n} = \\cfrac{1}{n!}";
	const exp_apprx = "e^x \\approx 1 + x + \\cfrac{x^2}{2!}";
	const fourier_series = "f(x) = \\sum_0^\\infty a_n\\cdot cos(nx) + b_n\\cdot sin(nx)";
	const fourier_coeffs= "\\cfrac{1}{T}\\int^T_0f(x)cos(nx)dx = a_n,\\ \\  \\cfrac{1}{T}\\int^T_0f(x)sin(nx)dx = b_n";
	const fourier_cosine_vector = "f(x) = \\left[{\\begin{array}{cccc} cos(0x) & cos(1x) & \\cdots & cos(nx) \\end{array}}\\right]     \\cdot     \\left[{\\begin{array}{c} a_0 \\\\ a_1 \\\\ \\vdots \\\\ a_n \\end{array}}\\right]";
	const fourier_sine_vector = "\\left[{\\begin{array}{cccc} sin(0x) & sin(1x) & \\cdots & sin(nx) \\end{array}}\\right]     \\cdot     \\left[{\\begin{array}{c} b_0 \\\\ b_1 \\\\ \\vdots \\\\ b_n \\end{array}}\\right]";
	const complex_coeffs = "c_n = \\left\\{ {\\begin{array}{ll} \\cfrac{a_n - ib_n}{2} & n \\ge 0 \\\\ \\cfrac{a_{-n} + ib_{-n}}{2} & n < 0 \\end{array}} \\right.";
	const freq_basis = "\\left[\\begin{array}{ccccc} e^{0} & e^{ix} & e^{i2x} & \\cdots & e^{inx}\\end{array}\\right]";

	const refs = ["https://youtu.be/3d6DsjIBzJ4"];
</script>

<main>

### Mapping Fourier Transform and Series

<img src={`${path}/joseph_fourier.webp`} alt="Joseph Fourier"/>

<hr>
<small> In this blog, we will investigate a new way of visualising Fourier transform and Series, which will help us further understand Quantum Mechanics' nature. </small>
<hr>

##### Taylor Series and Vector Spaces

Before getting into frequency space and Fourier transform, let us take a simple example of *Taylor's Series*.

Any *"well-behaved"* function can be written as an infinite series of polynomials.
<Eq eq={taylor_series} block/>

The coefficients are then found using a neat trick of differentiating on both sides.
<Eq eq={taylor_coeffs} block/>

One way of realising the Taylor series is that it is approximating a function with a polynomial.<sup>[[0]](#0)</sup>
However, there is another way of thinking about the Taylor series, a more *abstract* way.

Any <em data-tooltip="well-behaved">function</em> can be written as a **unique** Taylor Series. This also implies that every <em data-tooltip="well-behaved">function</em> is represented by its Taylor Series.
Since every Taylor Series is a polynomial series, one series is different from the other due to the coefficients. Thus:

"Every <em data-tooltip="well-behaved">function</em> is represented by an infinite list of its Taylor Coefficients."

<Eq eq={taylor_rep} block/>

If we take this representation as a vector in polynomial space, i.e. each basis <Eq eq="x_n"/> corresponds to each term of Taylor Series, <Eq eq="x^n"/> then the component on each basis is <Eq eq="a_n"/> (coefficient of the respective term in Series).

<Eq eq={taylor_vector} block/>

**Examples**
- Let <Eq eq="f(x) = 1 + 3x + 2x^2"/>:

Taylor coefficients are: <Eq eq="a_0 = 1, a_1 = 3, a_2 = 2, a_3 ... a_n = 0"/>. Hence, we require only 3-dimensional polynomial space to represent this.

<Frame name="taylor_ex1" path={path}/>

- Let <Eq eq="f(x) = sin(x)"/>:

Taylor expansion:

<Eq eq={sin_taylor} block/>

Taylor coefficients are <Eq eq={sin_coeff}/>. Hence, we require an infinite dimensional polynomial space to represent this.

Since it isn't possible to represent an infinite dimensional space, let us consider an approximation of sine, up to three "non-zero" coefficient terms, i.e. <Eq eq="a_1, a_3, a_5"/>.
With only these three terms, we can represent sine as a single point in 3D space, where <Eq eq="x = x^1, y = x^3, z = x^5"/>.

<Eq eq={sin_apprx} block/>

<Frame name="taylor_ex2" path={path}/>

- Let <Eq eq="f(x) = e^x"/>:

Taylor expansion:

<Eq eq={exp_taylor} block/>

Taylor coefficients are <Eq eq={exp_coeff}/>. Hence, we require an infinite dimensional polynomial space to represent this.

Let us consider an approximation of exponential, up to three "non-zero" coefficient terms, i.e. <Eq eq="a_0, a_1, a_2"/>.
With only these three terms, we can represent sine as a single point in 3D space, where <Eq eq="x = x^0, y = x^1, z = x^2"/>.

<Eq eq={exp_apprx} block/>

<Frame name="taylor_ex3" path={path}/>

Representing all the examples on single polynomial-space <Eq eq="x = x^0, y = x^1, z = x^2"/>:

<small>Note: for sine curve, the basis are <Eq eq="x = x^1, y = x^3, z = x^5"/></small>

<Frame name="taylor_ex_comb" path={path}/>

<small>

	Can you guess which point represents which curve?<span data-tooltip="red: sine,  yellow: exponential,  blue: polynomial" data-placement="right">...</span>

</small>
<hr>

**Representing more terms in Taylor space**
<Frame name="taylor_space" path={path}/>

<small>

Tip: use auto-scale for a better graph

In the above graph: <em>3rd order Taylor polynomial</em> there are 8 random points generated in Taylor space. Each point represents a polynomial with x, y, z corresponding to <Eq eq="a_0"/> <Eq eq="a_1"/> <Eq eq="a_2"/>.

In graph <em>5th order Taylor polynomial</em> there are 8 random points generated in Taylor space. Each point represents a polynomial with x, y, z, size, and colour corresponding to <Eq eq="a_0 ... a_4"/>.

</small>
<hr>

##### Fourier Series and Vector Spaces

Similar to the Taylor series, we can write any periodic <em data-tooltip="well-behaved">function</em> as a sum of cosines and sines of different <em data-tooltip="integer multiple of fundamental frequency" data-placement="bottom">harmonics</em>.

<Eq eq={fourier_series} block/>

The trick here to find the coefficient is to integrate <Eq eq="f(x)"/> after taking its product with the oscillatory component, i.e. <Eq eq="cos(nx)"/> or <Eq eq="sin(nx)"/>.

<Eq eq={fourier_coeffs} block/>

One way to realise the Fourier series is by wrapping the periodic function around a circle with an angular frequency of <Eq eq="n"/> and then finding the position of the centre of mass.<sup>[[1]](#1)</sup>

But going back to the analogy with the Taylor Series, similar to that, any function can be represented by its Fourier coefficients.
The only problem is that we need 2 infinite spaces, one for cosines and another for sine.

<Eq eq={fourier_cosine_vector + "+" + fourier_sine_vector} block/>

<Frame name="fs_kspace" path={path}/>
<small>

In graph <em>5th order Fourier series</em> there are 8 random points generated in Fourier space. Each point represents a series (harmonics) of sine wave (in blue) and cosine wave (in red) with x, y, z, size, and colour corresponding to <Eq eq="a_0"/> or <Eq eq="b_0 ... a_4"/> or <Eq eq="b_4"/>.

</small>

Since the Fourier series breaks a periodic function in harmonics of sines and cosines, we can call Fourier space frequency space, as it is a weighted sum of different frequencies of waves (harmonics).

To resolve the problem of 2 frequency spaces, for sines and cosines, we take the help of complex numbers.
Using Euler's formula, we write <Eq eq="sin"/> and <Eq eq="cos"/> in terms of <Eq eq="e"/>.

<Eq eq={String.raw`sin(nx) = \cfrac{e^{inx} - e^{-inx}}{2i}, \ \ cos(nx) = \cfrac{e^{inx} + e^{-inx}}{2} \ \ \  (1)`} block/>

On simplifying using (1):
<Eq eq={fourier_series + String.raw`= \sum_0^\infty c_n\cdot e^{inx}`} block/>
<small>

Here <Eq eq="c_n"/> is complex coefficient, with relation to <Eq eq="a_n, b_n"/> being: <Eq eq={complex_coeffs}/>

</small>

Now we only have one frequency space with <Eq eq={freq_basis}/> as its basis, <Eq eq="n \in \N + 0"/>.

<hr>
<Ref refs={refs}/>

</main>

<style>
	main
	{
		padding-top: 5%;
		padding-bottom: 5%;
		padding-left: 20%;
		padding-right: 20%;

		width: 100%;

		display: flex;
		flex-flow: column;

		overflow-y: scroll;
		overflow-x: hidden;
		scroll: smooth;
	}
	hr
	{
		width: 100%;
	}
	img
	{
		width: 100%;
		height: 50%;
		object-fit: none;
		object-position: center 30%;
	}
</style>
