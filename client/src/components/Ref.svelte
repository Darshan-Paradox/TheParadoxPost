<script>
	export let refs;
</script>

<h6>References:</h6>
{#each refs as ref, ind}
	<span id={ind}>
		{ind}: <em><a href={ref}>{ref}</a></em>
	</span>
{/each}

<style>
	span
	{
		font-size: 0.7rem;
	}
</style>
