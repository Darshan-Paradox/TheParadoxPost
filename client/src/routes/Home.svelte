<script>
	import ArrowRight from "carbon-icons-svelte/lib/ArrowRight.svelte";

	import RecentPost from "../components/RecentPost.svelte";
</script>

<div class="home-page">

	<div class="welcome-post">
		<h2>Welcome</h2>
		<em>Hi! I am Paradox.</em> My interest scales from <mark>Physics</mark> to <mark>Computer Sciences</mark> and this is my blog post, where I post insightful stuff I learned or came across.

		<br>
		<br>

		<a href="/bloglists" class="">
			<u>Show more</u>
			<ArrowRight />
		</a>

	</div>

	<RecentPost/>
</div>

<style>
	.home-page
	{
		width: 80%;
		padding-left: 2%;

		display: flex;
		flex-flow: row;
		justify-content: space-between;
		gap: 3px;
	}
</style>
