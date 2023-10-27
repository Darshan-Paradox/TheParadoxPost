<script>
	export let block = false;
	export let eq = "";

	import { math, display } from "mathlifier";

	let equation;
	equation = math(eq);

	if (block == true)
		equation = display(eq);
</script>

{@html equation}
