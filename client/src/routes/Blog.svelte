<script>
	import { onMount } from "svelte";

	export let params;

	async function get_blog()
	{
		let component;
		if (params.cat == "physics")
		{
			switch (params.id)
			{
				case "PlaneWavesFreeParticle":
					component = (await import("../blogs/physics/PlaneWavesFreeParticle.svelte.md")).default;
					break;
				case "FourierTransformVectorSpace":
					component = (await import("../blogs/physics/FourierTransformVectorSpace.svelte.md")).default;
			}
		}

		return component;
	}

	let blog = get_blog();
</script>

{#await blog}
	<div class="loading">
		<progress></progress>
	</div>
{:then component}
	<svelte:component this={component}>
	</svelte:component>
{/await}

<style>
	.loading
	{
		width: 25%;
		height: 100%;

		display: flex;
		justify-content: center;
		align-items: center;
	}
</style>
