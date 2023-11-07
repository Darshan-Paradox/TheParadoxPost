<script>
	export let block = false;
	export let eq = "";

	import { math, display } from "mathlifier";

	let equation;
	equation = math(eq);

	if (block == true)
		equation = display(eq);
</script>

{#if block}
	<p id="eq">
		{@html equation}
	</p>
{:else}
	{@html equation}
{/if}

<style>
	#eq
	{
		margin: 0px;
		padding: 0px;
		width: 100%;
		align-self: center;
	}
</style>
