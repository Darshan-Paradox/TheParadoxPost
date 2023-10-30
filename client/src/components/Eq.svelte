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
	<p>
		{@html equation}
	</p>
{:else}
	{@html equation}
{/if}
