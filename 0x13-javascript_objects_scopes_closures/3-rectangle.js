#!/usr/bin/node

class Rectangle{
	constructor (w, h){
		if ((w > 0) && (h > 0)) {
			this.width = w;
			this.width = h;
			}
		}
	print () {
	for (let x = 0; x < this.height; x++){
		let i  = '';
		for (let y = 0; y < this.width; y++){
		i += 'X';
		}
		console.log(i);
		}
	}
}
module.exports = Rectangle;
