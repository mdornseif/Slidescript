default:
	../pythonenv/bin/python ../slidec simple.slide --resolved test-simple.resolved
	cmp simple.resolved test-simple.resolved
	../pythonenv/bin/python ../slidec incomplete.slide --resolved test-incomplete.resolved
	cmp incomplete.resolved test-incomplete.resolved
	../pythonenv/bin/python ../slidec comment.slide --resolved test-comment.resolved
	cmp comment.resolved test-comment.resolved
	../pythonenv/bin/python ../slidec order.slide --resolved test-order.resolved
	cmp order.resolved test-order.resolved
	rm test-*.resolved
