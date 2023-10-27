<script>
	export let name;
	export let path;

	let src = `${path}/${name}.html`

	function resize(frame)
	{
		setTimeout(2000, ()=>{});

		frame.width = frame.contentWindow.document.body.scrollWidth;
		frame.height = frame.contentWindow.document.body.scrollHeight;

		frame.style.width = frame.contentWindow.document.body.scrollWidth + "px";
		frame.style.height = frame.contentWindow.document.body.scrollHeight + "px";
	}

	function resize_btn()
	{
		let frame = document.querySelector(`.${name}`);
		resize(frame);
	}
</script>

<div class="frame">
	<iframe src={src} title={name} class={name} on:load={(event) => {resize(event.target)}}>
	</iframe>
	<button class="contrast fit-content" on:click={()=>{resize_btn()}}>fit content</button>
</div>

<style>
	.frame
	{
		display: flex;
		flex-flow: column;
		justify-content: center;
		gap: 2px;

		align-self: center;
	}
	.fit-content
	{
		padding: 5px;
		width: fit-content;
		font-size: 0.6rem;
	}
</style>
