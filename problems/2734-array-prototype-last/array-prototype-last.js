/**
 * @return {null|boolean|number|string|Array|Object}
 */
Array.prototype.last = function() {
    let v=this.pop();
    return v !== undefined ? v: -1;
};

/**
 * const arr = [1, 2, 3];
 * arr.last(); // 3
 */