<script>
	import Eq from "../../components/Eq.svelte";
	import Frame from "../../components/Frame.svelte";

	import PlayFilledAlt from "carbon-icons-svelte/lib/PlayFilledAlt.svelte"

	import anime from "animejs";
	import { onMount } from "svelte";

	const plane_wave = "\\psi = A \\cdot e^{-i (kx - \\omega t)}";
	const normalisable_plane_wave = "\\int\\limits^{\\infty}_{-\\infty}\\psi = 1";
	const prob_density_plane_wave = "\\int\\limits^{\\infty}_{-\\infty}\\psi\\cdot\\psi^* \\ne 1";

	function disable(event, time)
	{
		event.target.disabled = true;
		setTimeout(() => {event.target.disabled = false}, time);
	}

	const path = `/blogs/physics/PlaneWavesFreeParticle`;
</script>

<main>

### <u>Why plane waves cannot represent free particles in Quantum Mechanics?</u>

As we know the equation of plane wave <Eq eq={plane_wave}/> is not normalisable, i.e. <Eq eq={normalisable_plane_wave} block/>
Thus the probability density <Eq eq={prob_density_plane_wave} block/>
This makes plane wave, a wrong description of a free particle, since the probability of it's exsistence cannot be <Eq eq="\infty" /> everywhere.

#### So what is the correct representation?

Consider, a free particle with momentum between <Eq eq="p_0"/> and <Eq eq="p_0+\Delta p"/>. At a given time <Eq eq="t_0"/>, we know it's location to be <Eq eq="x_0"/>. Therefore, after time <Eq eq="t_0+\Delta t"/> we know the location must be between <Eq eq="x_0"/> and <Eq eq="x_0+\Delta x"/>.

<Frame name="index" path={path}/>
<Frame name="scatter" path={path}/>

</main>

<style>
	main
	{
		padding-top: 5%;
		padding-bottom: 5%;
		padding-right: 25%;
		padding-left: 25%;
		display: flex;
		flex-flow: column;
		overflow: scroll;
	}
	p
	{
		align-self: center;
	}
</style>
