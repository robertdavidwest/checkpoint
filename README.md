# checkpoint
Easily and quickly shelve variables at some point in your code - a checkpoint! :)

Very similar to using a breakpoint in your code. For when you don't actually want to stop the code running and want to save the results after a crucial point

### Use Example

If you're code looks like this:

	some code here
	more here
	this takes ages to run...
	
	other stuff
	save results here

and you're worried something might break in `other stuff`. Add a checkpoint as follows:

	some code here
	more here
	this takes ages to run...
	import checkpoint; checkpoint.save()
	
	other stuff
	save results here

if you're code breaks in `other stuff` then load the checkpoint and you can begin debugging without having to run the slow section again:

	'''
	some code here
	more here
	this takes ages to run...
	'''
	import checkpoint; checkpoint.load()
	
	other stuff
	save results here

* `checkpoint.load()` will pick up the results of your most recent `checkpoint.save()`


### Noteworthy

* checkpoint will shelve your data at a default location that is defined in `checkpoint.py`. If you clone this repo I suggest updating this default location
* `checkpoint.save()` and `checkpoint.load()` do allow for directory overrides but for me this defeats the point as I want this to be super quick and simple to use. 