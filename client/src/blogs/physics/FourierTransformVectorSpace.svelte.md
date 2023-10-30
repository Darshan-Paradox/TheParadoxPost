<script>
	import Eq from "../../components/Eq.svelte";
	import Frame from "../../components/Frame.svelte";

	const path = `/blogs/physics/fourier_transform_vector_space`

	const fourier_series = "f(x) = \\sum_0^\\infty a_n\\cdot cos(nx) + b_n\\cdot sin(nx)";
</script>

<main>

### Mapping Fourier Transform and Series

<hr>
<small> In this blog we will investigate a new way of visualising Fourier transform and Series which will help us in further understanding the nature of Quantum Mechanics. </small>
<hr>

<Eq eq={fourier_series} block/>

<Frame name="fs_kspace" path={path}/>

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

		overflow: scroll;
	}
	hr
	{
		width: 100%;
	}
</style>
