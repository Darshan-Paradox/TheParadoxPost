<script>
	export let params;
	async function get_blog()
	{
		const component = (await import(`../blogs/${params.cat}/${params.id}.svelte.md`)).default;
		return component;
	}

	let blog = get_blog();
</script>

{#await blog then content}
	<svelte:component this={content}>
	</svelte:component>
{/await}
