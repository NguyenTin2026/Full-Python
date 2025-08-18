#TỔNG HỢP FULL KIẾN THỨC CẦN THIẾT VỀ NUMPY

""" import numpy as np
array = np.array([1,2,3,4])
array  = array / 2
print(array)
print(type(array)) """
#Bài 1: thư viên numpy
""" import numpy as np
array = np.array([1,2,3,4,5,6,7,8,9,10])
array = array * 10
print(array)
print(type(array)) """

#Bài 2: DIMENSIONS
'''import numpy as np
array = np.array(["A", "B", "C"])
print(array.ndim)'''
#hoặc
'''import numpy as np
array = np.array([["D", "E", "F"]])
print(array.ndim)'''
#hoặc 
'''import numpy as np
array = np.array([[["F", "G", "H"]]])
print(array.ndim)'''
#hoặc
'''import numpy as np
array = np.array([[[["I", "J", "K"]]]])
print(array.ndim)'''
#Tạo thành matrix
'''import numpy as np
array = np.array([['A', 'B', 'C'],
                 ['D', 'E', 'F'], 
                 ['G', 'H', 'I']])
print(array.ndim)'''
#Cách khác:
'''import numpy as np
array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'J']],
                  [['K', 'L', 'M'], ['N', 'O', 'P'], ['Q', 'R', 'S']],
                  [['T', 'U', 'V'], ['W', 'S', 'L'], ['Y', 'Z', '']]])
print(array.ndim)'''
# Multidimensional indexing is faster than chain indexing
'''import numpy as np
array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'J']],
                  [['K', 'L', 'M'], ['N', 'O', 'P'], ['Q', 'R', 'S']],
                  [['T', 'U', 'V'], ['W', 'S', 'L'], ['Y', 'Z', '']]])
print(array[0][0][0])'''  #hoặc có thể viết print(array[0, 0, 0])  #giải thích: số thứ nhất là cột, số thứ 2 là hàng, số thứ 3 là khối từ trái sang phải
'''import numpy as np
array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'J']],
                  [['K', 'L', 'M'], ['N', 'O', 'P'], ['Q', 'R', 'S']],
                  [['T', 'U', 'V'], ['W', 'S', 'L'], ['Y', 'Z', '']]])
print(array[2][0][0])'''  #hoặc có thể viết print(array[2, 0, 0])  #giải thích: số thứ nhất là cột, số thứ 2 là hàng, số thứ 3 là khối từ trái sang phải
#Luyện tập bất kỳ(ví dụ tạo tên là DO NGUYEN TIN TIN)
'''import numpy as np
array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'J']],
                  [['K', 'L', 'M'], ['N', 'O', 'P'], ['Q', 'R', 'S']],
                  [['T', 'U', 'V'], ['W', 'S', 'L'], ['Y', 'Z', 'I']]])
words = array[0,1,0] + array[1,1,1]  + array[1,1,0] + array[0,2,0] + array[2,0,1] + array[2,2,0] + array[0,1,1] + array[1,1,0] + array[2,0,0] + array[2,2,2] + array[1,1,0] + array[2,0,0] + array[2,2,2] + array[1,1,0] 
result = " ".join(words)
print(result)'''
# SLICING USING NUMPY
'''import numpy as np
array = np.array([[1,2,3,4], 
                 [5,6,7,8], 
                 [9,10,11,12], 
                 [13,14,15,16]])
#array[start:end:step]
print(array[0])'''
#Làm tiếp tục(chỉ có start)
'''import numpy as np
array = np.array([[1,2,3,4], 
                 [5,6,7,8], 
                 [9,10,11,12], 
                 [13,14,15,16]])
#array[start:end:step]
print(array[-1])'''      #Có thể dùng negative indexing bắt đầu từ -1
#Làm tiếp dạng khác(có start và enđ)
'''import numpy as np
array = np.array([[1,2,3,4], 
                 [5,6,7,8], 
                 [9,10,11,12], 
                 [13,14,15,16]])
#array[start:end:step]
print(array[0:4])'''   #Giải thích: số đầu tiên là start(bắt đầu từ số 0), số thứ 2 là end(đếm từ trên xuống bắt đầu số 1)

#Làm tiếp tục:
'''import numpy as np
array = np.array([[1,2,3,4], 
                 [5,6,7,8], 
                 [9,10,11,12], 
                 [13,14,15,16]])
#array[start:end:step]
print(array[1:4])'''   #Giải thích: số đầu tiên là start(đếm từ trên xuống bắt đầu từ số 0), số thứ 2 là end(đếm từ trên xuống bắt đầu số 1)

#Làm tiếp tục:(có start:)
'''import numpy as np
array = np.array([[1,2,3,4], 
                 [5,6,7,8], 
                 [9,10,11,12], 
                 [13,14,15,16]])
#array[start:end:step]
print(array[1:])'''

#Làm tiếp tục(có start:end:step)
'''import numpy as np
array = np.array([[1,2,3,4], 
                 [5,6,7,8], 
                 [9,10,11,12], 
                 [13,14,15,16]])
#array[start:end:step]
print(array[0:4:2])'''
#Làm tiếp tục(có start:end:step)
'''import numpy as np
array = np.array([[1,2,3,4], 
                 [5,6,7,8], 
                 [9,10,11,12], 
                 [13,14,15,16]])
#array[start:end:step]
print(array[0:4:3])'''
#Làm tiếp tục(có start:end:step)
'''import numpy as np
array = np.array([[1,2,3,4], 
                 [5,6,7,8], 
                 [9,10,11,12], 
                 [13,14,15,16]])
#array[start:end:step]
print(array[::2])'''
#Làm tiếp tục(có start:end:step)
'''import numpy as np
array = np.array([[1,2,3,4], 
                 [5,6,7,8], 
                 [9,10,11,12], 
                 [13,14,15,16]])
#array[start:end:step]
print(array[::-1])'''
#Làm tiếp tục(có start:end:step)
'''import numpy as np
array = np.array([[1,2,3,4], 
                 [5,6,7,8], 
                 [9,10,11,12], 
                 [13,14,15,16]])
#array[start:end:step]
print(array[:,0])'''
#Làm tiếp tục(có start:end:step)
'''import numpy as np
array = np.array([[1,2,3,4], 
                 [5,6,7,8], 
                 [9,10,11,12], 
                 [13,14,15,16]])
#array[start:end:step]
print(array[:,1])'''
#Làm tiếp tục(có start:end:step)
'''import numpy as np
array = np.array([[1,2,3,4], 
                 [5,6,7,8], 
                 [9,10,11,12], 
                 [13,14,15,16]])
#array[start:end:step]
print(array[:,-1])'''
#Làm tiếp tục(có start:end:step)
'''import numpy as np
array = np.array([[1,2,3,4], 
                 [5,6,7,8], 
                 [9,10,11,12], 
                 [13,14,15,16]])
#array[start:end:step]
print(array[:,-2])'''
#Làm tiếp tục(có start:end:step)
'''import numpy as np
array = np.array([[1,2,3,4], 
                 [5,6,7,8], 
                 [9,10,11,12], 
                 [13,14,15,16]])
#array[start:end:step]
print(array[:,1:4])'''    #số đầu tiên là start(đếm từ trên xuống bắt đầu từ số 0), số thứ 2 là end(đếm từ trên xuống bắt đầu số 1)
#Làm tiếp tục(có start:end:step)
'''import numpy as np
array = np.array([[1,2,3,4], 
                 [5,6,7,8], 
                 [9,10,11,12], 
                 [13,14,15,16]])
#array[start:end:step]
print(array[:, ::2])'''  #Giải thích: số 2 là step
#Làm tiếp tục(có start:end:step)
'''import numpy as np
array = np.array([[1,2,3,4], 
                 [5,6,7,8], 
                 [9,10,11,12], 
                 [13,14,15,16]])
#array[start:end:step]
print(array[:, 1::2])'''
#Làm tiếp tục(có start:end:step)
'''import numpy as np
array = np.array([[1,2,3,4], 
                 [5,6,7,8], 
                 [9,10,11,12], 
                 [13,14,15,16]])
#array[start:end:step]
print(array[:, ::-1])
#Làm tiếp tục(có start:end:step)
import numpy as np
array = np.array([[1,2,3,4], 
                 [5,6,7,8], 
                 [9,10,11,12], 
                 [13,14,15,16]])
#array[start:end:step]
print(array[:, ::-2])'''
#Làm tiếp tục(có start:end:step)
'''import numpy as np
array = np.array([[1,2,3,4], 
                 [5,6,7,8], 
                 [9,10,11,12], 
                 [13,14,15,16]])
#array[start:end:step]
print(array[0:2, 0:2])''' #Giải thích: Số đầu tiên(0) đếm bắt đầu từ 0, số thứ hai(2) đếm bắt đầu từ 1 ; trước dấu , là start ; sau dấu , là end'

#SCALAR ARITHMETIC IN NUMPY
#Scalar is a linear algebra term
'''import numpy as np
array =np.array([1,2,3])
print(array + 1)
print(array -2)
print(array * 4)
print(array / 3)
print(array ** 6)'''

#VECTORIZED MATH FUNCTIONS IN NUMPY
'''array = np.array([1,2,3])
print(np.sqrt(array))'''
#Làm tròn số truyền thống(>= 5) dùng round
'''array = np.array([1.0002, 2.96, 123.3121, 432.442])
print(np.round(array))'''
#Làm tròn số xuống dùng floor
'''array = np.array([1.0002, 2.96, 123.3121, 432.442])
print(np.floor(array))'''
# Làm tròn lên dùng ceil
'''array = np.array([1.0002, 2.96, 123.3121, 432.442])
print(np.ceil(array))'''
#Làm tròn số pi(~3,14159)
'''import numpy as np
print(np.pi)'''
# Kết hợp pi với array và phép tính
'''import numpy as np
radius = np.array([1,2,3])
print(np.pi * radius ** 2)'''

# Elemet-wise arithmetic
'''import numpy as np
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])
print(array1 + array2)  #Có thể dùng các phép toán khác như - * / ** //
print(array1 - array2)
print(array1 * array2)
print(array1 / array2)
print(array1 ** array2)'''

# Comparison operators
'''import numpy as np
scores = np.array([91, 55, 100, 73, 82, 64])
print(scores == 100)'''  #Có thể thêm các điều kiện khác như > < >= <= !=

#Làm kiểu khác
'''import numpy as np
scores = np.array([91, 55, 100, 73, 82, 59, 89])
scores[scores < 60] = 0
print(scores)'''

# Broadcasting allows Numpy to perform operations on arrays
# with different shapes by virtually expanding dimensions
# so they match the larger array's shape
# The dimensions have the same size
# OR One of the dimensions has a size of 1
# shape dùng để tìm ra bao nhiêu hàng bao nhiêu cột
'''import numpy as np
array1 = np.array([[1,2,3,4]])
array2 = np.array([[1], [2], [3], [4]])
print(array1.shape)     #Mảng array1 có 1 hàng và 4 cột
print(array2.shape)     #Mảng array2 có 4 hàng và 1 cột'''
#Có thể thêm số vào array1 tùy thích
'''import numpy as np
array1 = np.array([[1,2,3,4],
                   [5,6,7,8]])
array2 = np.array([[1], [2], [3], [4]])
print(array1.shape)  #Mảng array1 có 2 hàng và 4 cột
print(array2.shape)  #Mảng array2 có 4 hàng 1 cột'''
#Có thể thêm số vào array2 tùy thích
'''import numpy as np
array1 = np.array([[1,2,3,4]])
array2 = np.array([[1], [2], [3], [4],
                  [5], [6], [7], [8]])    
print(array1.shape)  #Mảng array1 có 1 hàng và 4 cột
print(array2.shape)  #Mảng array2 có 8 hàng và 1 cột'''
#Luyện tập 1 bài nữa về array1 và array2
'''import numpy as np
array1 = np.array([[1,2,3,4,5,6,7,8,9,10]])
array2 = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
print(array1.shape)  #Mảng array1 có 1 hàng và 10 cột
print(array2.shape)  #Mảng array2 có 10 hàng và 1 cột'''
#Chúng ta có thể dùng  + - * / ** // % sqrt abs absolute fabs  giữa array1 và array2
'''import numpy as np
array1 = np.array([[1,2,3,4,5,6,7,8,9,10]])
array2 = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
print(array1 * array2) #có thể print(np.sqrt(array1)), print(np.abs(array2)), ... '''

# Aggregate functions = summarize data and typically return a single value
'''import numpy as np
array = np.array([[1,2,3,4,5],
                 [6,7,8,9,10]])
#print(np.sum(array)) hoặc #print(np.sum(array, axis = con số)) #axis chỉ có 2 con số là 0 và 1 #nếu axis = 0 thì thực hiện phép toán theo chiều dọc, nếu axis = 1 thì thực hiện phép toán theo chiều ngang.
#print(np.mean(array))
#print(np.std(array))
#print(np.var(array))
#print(np.max(array))
#print(np.min(array))
#print(np.argmax(array))
#print(np.argmin(array)) '''

# Filtering = Refers to the process of selecting elements from an array that match a given condition
'''import numpy as np
ages = np.array([[11,18,19,22,23,26,30,32,54,43,46],
                 [2,17,16,13,23,65,76,85,97,45,41]])
teenagers = ages[ages < 18]
print(teenagers)
#Có thể thêm điều kiện khác để lọc ra
adults = ages[ages >= 18]
print(adults)
#Thêm nhiều điều kiện cùng lúc
peoples = [(ages >= 18) & (ages <= 65)]  #ngoài kí hiệu & có thể dùng  and  hoặc  |
print(peoples)
#Làm thêm cho senior
seniors = ages[ages >= 65]
print(seniors)
#Làm thêm ví dụ evens
evens = ages[ages % 2 == 0]
print(evens)
#Làm thêm ví dụ odds
odds = ages[ages % 2 != 0]
print(odds)
#Có thể dùng từ khóa  where  để lọc bằng cách đặt điều kiện trong Python
#Ví dụ cho adults
adults = np.where(ages >= 18, ages, 0) #Giải thích: nếu điều kiện đúng=> ages được giữ nguyên, nếu điều kiện sai=>giá trị được thay thế bằng 0.
print(adults)'''

#Creating Random Numbers in NUMPY
'''import numpy as np
rng = np.random.default_rng()
print(rng.integers(1, 7)) # hoặc print(rng.integers(low=1, high=101, size = số))  #dùng size = con số bất kì, nghĩa là nó sẽ in ra con số hoặc những số ngẫu nhiên tùy vào size mình chọn.
                          # Nếu size = (số x, số y)  #Giải thích: x là số hàng, y là số cột '''
# Có thể thêm seed vào random numbers
'''import numpy as np
rng = np.random.default_rng(seed = 1) #Cú pháp là seed = value (giúp tái tạo kết quả ngẫu nhiên trong các thí nghiệm hoặc mô phỏng)
print(rng.integers(1, 7)) '''       

#Từ khóa uniform trong NUMPY
'''import numpy as np
print(np.random.uniform()) #Giải thích: từ khóa uniform nếu không gán giá trị thì nó sẽ mặc định lấy số ngẫu nhiên trong phạm vi từ 0-->1((bao gồm số thập phân))
                           #Nếu gán giá trị thì nó sẽ tuân theo giá trình mình gán '''
#Luyện tập
'''import numpy as np
np.random.seed(seed=1)
print(np.random.uniform(low=-1, high=1, size=(5, 8))) '''

#Kết hợp array với random numbers + từ khóa shuffle(xáo trộn) các con số ngẫu nhiên trong NUMPY
'''import numpy as np
rng = np.random.default_rng() 
array = np.array([1,2,3,4,5])
rng.shuffle(array)   #Giải thích: shuffle dùng để xóa trộn số một cách ngẫu nhiên.
print(array) '''

#Luyện tập xáo trộn giá trị ngẫu nhiên dạng văn bản
'''import numpy as np
rng = np.random.default_rng()
family = np.array(["Tin Tin", "Tin Tín", "Tin Tưởng", "Ba Cường", "Má Phương"])
rng.shuffle(family)  #hoặc có thể ghi family = rng.shuffle(family) ==> print(family)
print(family) '''
#Dùng từ khóa choice để lấy ngẫu nhiên ra 1 item
import numpy as np
rng = np.random.default_rng()
family = np.array(["Tin Tin", "Tin Tín", "Tin Tưởng", "Ba Cường", "Má Phương"])
family = rng.choice(family)  #hoặc có thể ghi family = rng.choice(family) ==> print(family)  #Có thể thêm size vào ví dụ: family = rng.choice(family, size(3,5))
print(family)

#BÀI TẬP: Thay vì dùng văn bản random chán có thể dùng hình dán(emoji) để gán vào cho nó thú vị hơn.

#__________________________________________________Hết____________________________________________________________