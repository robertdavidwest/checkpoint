# checkpoint
Easily and quickly shelve variables at some point in your code - a checkpoint! :)

Very similar to using a breakpoint in your code. For when you don't actually want to stop the code running and want to save the results after a crucial point

* Saving all local variables: 

		checkpoint.save(locals())
		
* Loading the most recently saved set of variables and adding back into the local namespace:

		locals().update(checkpoint.load())
	
### Use Example - Shelving all local variables

If you're code looks like this:

	some code here
	more here
	this takes ages to run...
	
	other stuff
	save results here

and you're worried something might break in `other stuff`. Add a checkpoint as follows:
	
	import checkpoint
	
	some code here
	more here
	this takes ages to run...
	checkpoint.save(locals())
	
	other stuff
	save results here

if you're code breaks in `other stuff` then load the checkpoint and you can begin debugging without having to run the slow section again:

	import checkpoint
	
	'''
	some code here
	more here
	this takes ages to run...
	'''	 
	locals().update(checkpoint.load())
	
	other stuff
	save results here

* `checkpoint.load()` will pick up the results of your most recent `checkpoint.save()`

### To shelve a specific variable instead or set of variables just pass a dict:

* `checkpoint.save({'df': df})`
* `locals.update(checkpoint.load())`

### Important

* No variables with `__` in the variable name will be stored. Keep that in mind when using.

### Noteworthy

* checkpoint will shelve your data at a default location that is defined in `checkpoint.py`. If you clone this repo I suggest updating this default location
* `checkpoint.save()` and `checkpoint.load()` do allow for directory overrides but for me this defeats the point as I want this to be super quick and simple to use. 