<script>
	//CODE to FETCH RECENT POSTS
	async function get_posts()
	{
		const URL = "https://the-paradox-post-api.vercel.app/api/recentposts";
		const response = await fetch(URL);
		const posts = await response.json();
		return posts;
	}

	let posts = get_posts();
</script>

<div class="recent-posts">
<h3>Recent Articles</h3>
{#await posts then posts_list}
	<ul>
		{#each posts_list as post}
			<li>
				<a href={post.link}>
					{post.title}
				</a>
			</li>
		{/each}
	</ul>
{/await}
</div>

<style>
	.recent-posts
	{
		width: 40%;

		display: flex;
		flex-flow: column;
		gap: 2px;
	}
</style>
