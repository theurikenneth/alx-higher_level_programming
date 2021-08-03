#!/usr/bin/node
// Initializes a Rectangle class with height and width
class Rectangle {
  constructor (w, h) {
    if ((w = parseInt(w)) > 0 && (h = parseInt(h)) > 0) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
