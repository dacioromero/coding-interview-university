# Arrays
An object containing, same-size (primitive or objects), indexed, elements in continous space of memory

## Multi-dimensional
arrays that allow coordinates (e.g. (x,y)); still constant time using math

## Timing
|        | Add  | Remove |
| ------ | ---- | ------ |
| Start  | O(n) | O(n)   |
| End    | O(1) | O(1)   |
| Middle | O(n) | O(n)   |

## Dynamic
Solves the problem of not knowing how many elements will exist in array

Composedo of a static array that is replaced with another appropriate-sized when needed

## Jagged
Aka. array of arrays. First array is fixed, size which contains other arrays which can be varying sizes; making it "jagged."
