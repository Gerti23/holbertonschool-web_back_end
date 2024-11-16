# ES6 Basics

This repository contains several JavaScript tasks focused on ES6 features. Each task is implemented in a separate JavaScript file.

## Table of Contents

1. [Const or let?](#const-or-let)
2. [Block Scope](#block-scope)
3. [Arrow Functions](#arrow-functions)
4. [Parameter Defaults](#parameter-defaults)
5. [Rest Parameter Syntax for Functions](#rest-parameter-syntax-for-functions)
6. [The Wonders of Spread Syntax](#the-wonders-of-spread-syntax)
7. [Take Advantage of Template Literals](#take-advantage-of-template-literals)
8. [Object Property Value Shorthand Syntax](#object-property-value-shorthand-syntax)
9. [No Need to Create Empty Objects Before Adding Properties](#no-need-to-create-empty-objects-before-adding-properties)
10. [ES6 Method Properties](#es6-method-properties)
11. [For...of Loops](#forof-loops)
12. [Iterator](#iterator)
13. [Let's Create a Report Object](#lets-create-a-report-object)

## Const or let?

Functions to instantiate variables using `const` and `let`.

- **Prototype:**
  - `function taskFirst()`
  - `function taskNext()`
- **File:** [0-constants.js](0-constants.js)

## Block Scope

Modify the variables inside the function `taskBlock` so that the variables aren’t overwritten inside the conditional block.

- **File:** [1-block-scoped.js](1-block-scoped.js)

## Arrow Functions

Rewrite the following standard function to use ES6’s arrow syntax of the function `add`.

- **File:** [2-arrow.js](2-arrow.js)

## Parameter Defaults

Condense the internals of the following function to 1 line by defining default parameter values for the function parameters.

- **File:** [3-default-parameter.js](3-default-parameter.js)

## Rest Parameter Syntax for Functions

Modify the following function to return the number of arguments passed to it using the rest parameter syntax.

- **File:** [4-rest-parameter.js](4-rest-parameter.js)

## The Wonders of Spread Syntax

Using spread syntax, concatenate 2 arrays and each character of a string by modifying the function below. The function body should be one line long.

- **File:** [5-spread-operator.js](5-spread-operator.js)

## Take Advantage of Template Literals

Rewrite the return statement to use a template literal to substitute the variables you’ve defined.

- **File:** [6-string-interpolation.js](6-string-interpolation.js)

## Object Property Value Shorthand Syntax

Modify the function’s budget object to use the object property value shorthand syntax.

- **File:** [7-getBudgetObject.js](7-getBudgetObject.js)

## No Need to Create Empty Objects Before Adding Properties

Rewrite the `getBudgetForCurrentYear` function to use ES6 computed property names on the budget object.

- **File:** [8-getBudgetCurrentYear.js](8-getBudgetCurrentYear.js)

## ES6 Method Properties

Rewrite `getFullBudgetObject` to use ES6 method properties in the fullBudget object.

- **File:** [9-getFullBudget.js](9-getFullBudget.js)

## For...of Loops

Rewrite the function `appendToEachArrayValue` to use ES6’s for...of operator.

- **File:** [10-loops.js](10-loops.js)

## Iterator

Write a function named `createEmployeesObject` that will receive two arguments: `departmentName` (String) and `employees` (Array of Strings).

- **File:** [11-createEmployeesObject.js](11-createEmployeesObject.js)

## Let's Create a Report Object

Write a function named `createReportObject` whose parameter, `employeesList`, is the return value of the previous function `createEmployeesObject`.

- **File:** [12-createReportObject.js](12-createReportObject.js)
