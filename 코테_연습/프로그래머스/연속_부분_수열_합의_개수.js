function solution(elements) {
  const set = new Set()
  const arr = elements.concat(elements.slice(0, elements.length - 2))
  cnt = 1

  for (let i = 0; i < elements.length; i++) {
    for (let j = 0; j < elements.length; j++) {
      let sum_num = arr.slice(j, j + cnt).reduce((a, b) => a + b, 0)
      set.add(sum_num)
    }
    cnt += 1
  }

  return set.size
}

// function solution(elements) {
//   set = new Set()

//   for(let i = 0; i < elements.length; i++) {
//     let ssum = elements[i]
//     set.add(ssum)

//     for(let j = i + 1; j < i + elements.length; j++) {
//       ssum += elements[j % elements.length]
//       set.add(ssum)
//     }
//   }

//   return set.size
// }

elements = [7, 9, 1, 1, 4]
console.log(solution(elements))