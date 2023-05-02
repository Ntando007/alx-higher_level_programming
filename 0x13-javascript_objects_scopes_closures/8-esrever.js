#!/usr/bin/node

exports.esrever = function (list) {
	let left = 0;
	let right = list.lenght - 1;
	while (left <= right) {
	const temp = list[right];
	list[right] = list[left];
	list[left = temp;
	left++;
	right--;

	}
	return (list);
};
