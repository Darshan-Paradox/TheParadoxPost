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

	const refs = ["https://youtu.be/3d6DsjIBzJ4"];
</script>

<main>

### Mapping Fourier Transform and Series

<hr>
<small> In this blog we will investigate a new way of visualising Fourier transform and Series which will help us in further understanding the nature of Quantum Mechanics. </small>
<hr>

##### Taylor Series and Vector Spaces

Before getting into, frequency space and fourier tranforms, let us take a simple example of *Taylor's Series*.

Any *"well-behaved"* function can be written as infinite series of polynomial.
<Eq eq={taylor_series} block/>

The coefficients are then found by using a neat trick of differentiating on both sides.
<Eq eq={taylor_coeffs} block/>

One way of realising taylor series is that it is approximating a function with a polynomial.<sup>[[0]](#0)</sup>
Though there is another way of thinking about taylor series, a more *abstract* way.

Any <em data-tooltip="well-behaved">function</em> can be written as an **unique** Taylor Series. Which also implies that every <em data-tooltip="well-behaved">function</em> is represented by its Taylor Series.
Since every Taylor Series is a series of polynomial, one series is different from other due to the coefficients. Thus:

"Every <em data-tooltip="well-behaved">function</em> is represented by an infinite list of it's Taylor Coefficients."

<Eq eq={taylor_rep} block/>

If we take this representation as a vector in polynomial space, i.e. each basis <Eq eq="x_n"/> corresponds to each term of Taylor Series, <Eq eq="x^n"/> then the component on each basis is <Eq eq="a_n"/> (coefficient of respective term in Series).

<Eq eq={taylor_vector} block/>

**Examples**
- Let <Eq eq="f(x) = 1 + 3x + 2x^2"/>:

Taylor coefficients are : <Eq eq="a_0 = 1, a_1 = 3, a_2 = 2, a_3 ... a_n = 0"/>, hence we require only 3-dimensional polynomial space to represent this.

<Frame name="taylor_ex1" path={path}/>

- Let <Eq eq="f(x) = sin(x)"/>:

Taylor expansion:

<Eq eq={sin_taylor} block/>

Taylor coefficients are : <Eq eq={sin_coeff}/>, hence we require an infinite dimensional polynomial space to represent this.

Since it isn't possible to represent an infinite dimensional space, let us consider an approximation of sine, upto three "non-zero" coefficient terms, i.e. <Eq eq="a_1, a_3, a_5"/>.
With only these three terms, we can represent sine as a single point in 3D space, where <Eq eq="x = x^1, y = x^3, z = x^5"/>.

<Eq eq={sin_apprx} block/>

<Frame name="taylor_ex2" path={path}/>

- Let <Eq eq="f(x) = e^x"/>:

Taylor expansion:

<Eq eq={exp_taylor} block/>

Taylor coefficients are : <Eq eq={exp_coeff}/>, hence we require an infinite dimensional polynomial space to represent this.

Since it isn't possible to represent an infinite dimensional space, let us consider an approximation of sine, upto three "non-zero" coefficient terms, i.e. <Eq eq="a_0, a_1, a_2"/>.
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

**Representing more terms in taylor space**
<Frame name="taylor_space" path={path}/>

<small>

Tip: use auto-scale for better graph

In above graph: <em>3rd order taylor polynomial</em> there are 8 random points generated in taylor space. Each point represents a polynomial with x, y, z corresponding to <Eq eq="a_0"/> <Eq eq="a_1"/> <Eq eq="a_2"/>.

In graph: <em>5th order taylor polynomial</em> there are 8 random points generated in taylor space. Each point represents a polynomial with x, y, z,size,color corresponding to <Eq eq="a_0 ... a_4"/>.

</small>
<hr>

<Eq eq={fourier_series} block/>

<Frame name="fs_kspace" path={path}/>

<hr>
<Ref refs={refs}/>

</main>

<style>
	main
	{
		padding-top: 5%;
		padding-bottom: 5%;
		padding-left: 25%;
		padding-right: 25%;

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
</style>
