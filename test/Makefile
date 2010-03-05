default:
	../pythonenv/bin/python ../slidec simple.slide --resolved test-simple.resolved
	cmp simple.resolved test-simple.resolved
	../pythonenv/bin/python ../slidec incomplete.slide --resolved test-incomplete.resolved
	cmp simple.resolved test-simple.resolved
	../pythonenv/bin/python ../slidec comment.slide --resolved comment.resolved
	cmp simple.resolved test-simple.resolved
	rm test-*.resolved
