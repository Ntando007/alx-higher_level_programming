#!/usr/bin/node

class Rectangle{
	constructor (w, h){
	if ((w > 0) && (h > 0)){
		this.width = w;
		this.height =h;
	}
	}
	
	print() {
	for (let x = 0; x < this.height; x++){
	let i = '';
	for (let y = 0; y < this.width; y++) {
	i += 'X';
	}
	console.log(s);
	}
	}

	rotate () {
	const aux = this.width;
	this.width = this.height;
	this.height = aux;
	}

	double () {
	this.width *= 2;
	this.height *= 2;
	}
}

module.exports = Rectangle;
