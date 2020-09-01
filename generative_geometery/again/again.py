for i in range(0, 50):
	plot(ctx, shapes.spiro(5, 10, 4), .05, (i * .001, i * .01, i * .02))
	ctx.rotate(5)