# Journey into JavaScript: Objects, Scopes, and Closures

## Function Blueprints 🚀

Functions in this project come with unique blueprints:

| File               | Function Signature                                     |
| ------------------ | ------------------------------------------------------- |
| `7-occurrences.js` | `exports.countOccurrences = function (list, searchElement)` |
| `8-esrever.js`     | `exports.reverseList = function (list)`                     |
| `9-logme.js`       | `exports.logWithCount = function (item)`                       |
| `10-converter.js`  | `exports.convertBase = function (base)`                   |


## Exploring the Code 📝

* **0. Creating the Blank Canvas - Rectangle #0**
  * [0-rectangle.js](./0-rectangle.js): A JavaScript script that lays the foundation with an empty
  class named `Rectangle`.

* **1. Building Blocks - Rectangle #1**
  * [1-rectangle.js](./1-rectangle.js): This JavaScript script introduces a class
  `Rectangle`. It builds upon [0-rectangle.js](./0-rectangle.js) with:
    * A constructor that initializes instance attributes `width` and `height` using
    given parameters `w` and `h`.

* **2. Defensive Building - Rectangle #2**
  * [2-rectangle.js](./2-rectangle.js): In this JavaScript script, we refine the class
  `Rectangle` further, building on [1-rectangle.js](./1-rectangle.js) by ensuring that
  if provided `w` and `h` are less than or equal to `0`, an empty object is created.

* **3. Printing the Blueprint - Rectangle #3**
  * [3-rectangle.js](./3-rectangle.js): A JavaScript script that enhances the class
  `Rectangle` from [3-rectangle.js](./3-rectangle.js) with:
    * An instance method `print()` that visualizes the rectangle using the `X` character.

* **4. Architect's Touch - Rectangle #4**
  * [4-rectangle.js](./4-rectangle.js): The JavaScript script for this task brings sophistication
  to the class `Rectangle` defined in [4-rectangle.js](./4-rectangle.js) with:
    * Instance methods `rotate()` and `double()` that transform the dimensions of the `Rectangle`.
    * `rotate()` swaps the `width` and `height`, while `double()` multiplies them by `2`.

* **5. Square Magic - Square #0**
  * [5-square.js](./5-square.js): In this JavaScript script, a class `Square`
  is introduced, inheriting from `Rectangle`.
    * The constructor now takes one argument `size`.

* **6. Shaping the Square - Square #1**
  * [6-square.js](./6-square.js): Extending the class `Square` from [5-square.js](./5-square.js),
  this script adds an instance method `charPrint(c)` for custom character printing.
    * If `c` is `undefined`, the character `X` is used.

* **7. Counting Occurrences - Occurrences**
  * [7-occurrences.js](./7-occurrences.js): A JavaScript function that computes and returns the
  number of occurrences in a list.

* **8. The List Reversal - Esrever**
  * [8-esrever.js](./8-esrever.js): A JavaScript function that elegantly reverses a list.

* **9. Logging the Odyssey - Log me**
  * [9-logme.js](./9-logme.js): A JavaScript function that logs the number of
  arguments already printed along with the new argument value.
  * Output: `<number arguments already printed>: <current argument value>`

* **10. Base Converter - Number Conversion**
  * [10-converter.js](./10-converter.js): A JavaScript function that embarks on the journey of converting a number
  from base 10 to another base passed as an argument.

* **11. Mapping the Journey - Factor Index**
  * [100-map.js](./100-map.js): A JavaScript script that navigates through an array, creating
  a new array with each value equal to the product of the value of the initial list times the index of
  the new list.
  * Both the initial and new lists are printed.

* **12. Sorted Chronicles - Sorted Occurrences**
  * [101-sorted.js](./101-sorted.js): A JavaScript script that delves into the lore of a dictionary,
  computing a new dictionary of user IDs by occurrences.
  * The new dictionary is unveiled.

* **13. Harmonious Concatenation - Concat Files**
  * [102-concat.js](./102-concat.js): A JavaScript script that orchestrates the harmonious concatenation of two files
  passed as arguments into a file specified as the third argument.
  * Usage: `./102-concat.js fileA fileB fileC`.
