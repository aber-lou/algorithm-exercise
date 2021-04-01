class Solution {
    func clumsy(_ N: Int) -> Int {
        if N == 1 {
            return 1
        }

        var arr = Array<String>()
        var num = N
        var index = 1

        arr.append(String(num))

        while (num > 1) {
            let temp = num - 1
            switch (index) {
            case 1: do {
                let value = Int(arr.popLast()!)! * temp
                arr.append(String(value))
            }
            case 2: do {
                let value = Int(arr.popLast()!)! / temp
                arr.append(String(value))
            }
            case 3: do {
                arr.append(String(temp))
            }
            case 4: do {
                arr.append(String(-temp))
            }
            default: continue
            }    

            if (index < 4) {
                index += 1
            } else {
                index = 1
            }
            num -= 1
        }

        var result = 0;
        for char in arr {
            result += Int(char)!
        }

        return result
    }
}