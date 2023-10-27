<script>
	import { onMount } from "svelte";

	export let params;

	async function get_blog()
	{
		const component = (await import(`../blogs/${params.cat}/${params.id}.svelte.md`)).default;
		return component;
	}

	let blog = null;

	onMount(async () => {blog = await get_blog()})
</script>

<svelte:component this={blog}>
</svelte:component>
