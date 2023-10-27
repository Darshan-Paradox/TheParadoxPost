<script>
	import FunctionMath from "carbon-icons-svelte/lib/FunctionMath.svelte";
	import Code from "carbon-icons-svelte/lib/Code.svelte";

	let topic = 0;

	//make this async fetching
	async function bloglists()
	{
		const response = await fetch("http://127.0.0.1:5000/api/bloglists");
		const content = await response.json();

		return content;
	}

	let blogs = bloglists();
</script>

<div class="switcher">
	<button class="contrast outline" on:click={() => {topic = 0}}>
		<div class="switch-label">
			<FunctionMath />
			Physics
		</div>
	</button>
	<button class="contrast outline" on:click={() => {topic = 1}}>
		<div class="switch-label">
			<Code />
			Programming
		</div>
	</button>
	<button class="contrast outline" on:click={() => {topic = 2}}>
		<div class="switch-label">
			Misc
		</div>
	</button>
</div>
<article>
	{#await blogs then titles}
		<ul>
			{#if titles[topic].length == 0}
				No blogs uploaded yet
			{/if}

			{#each titles[topic] as blog}
				<li>
					<a href="">
						{blog}
					</a>
				</li>
			{/each}
		</ul>
	{/await}
</article>

<nav aria-label="breadcrumb">
  <ul>
<li><a href="/">Home</a></li>
    <li>Blog List</li>
  </ul>
</nav>


<style>
	nav
	{
		align-self: center;
	}
	.switcher
	{
		width: 50%;

		display: flex;
		flex-flow: row;
		align-items: center;
		gap: 5px;
	}

	.switch-label
	{
		display: flex;
		flex-flow: row;
		justify-content: center;
		align-items: center;
		gap: 5px;
	}
</style>
