function solution(operations) {
  const answer = []

  operations.forEach(operation => {
    let [order, number] = operation.split(' ')
    number = parseInt(number)

    if (order === 'I') {
      answer.push(number)
    } else {
      if (!answer.length) return
      let val = (number === -1 ? Math.min : Math.max)(...answer)
      let idx = answer.findIndex(value => value === val)

      answer.splice(idx, 1)
    }
  })

  return answer.length ? [Math.max(...answer), Math.min(...answer)] : [0, 0]
}

operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
console.log(solution(operations))