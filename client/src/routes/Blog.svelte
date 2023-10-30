<script>
	import { onMount } from "svelte";

	export let params;

	async function get_blog()
	{
		let component;
		if (params.cat == "physics")
			if (params.id == "PlaneWavesFreeParticle")
				component = (await import("../blogs/physics/PlaneWavesFreeParticle.svelte.md")).default;
			if (params.id == "FourierTransformVectorSpace")
				component = (await import("../blogs/physics/FourierTransformVectorSpace.svelte.md")).default;
		return component;
	}

	let blog = null;

	onMount(async () => {blog = await get_blog()})
</script>

<svelte:component this={blog}>
</svelte:component>
