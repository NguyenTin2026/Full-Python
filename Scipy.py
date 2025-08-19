@  SCIPY TUTORIAL  @
- Scipy là một thư viện tính toán khoa học sử dụng Numpy bên dưới.
- Scipy là viết tắt của Scientific Python.
- Scipy bao gồm các tính năng tiện ích như: tối ưu hóa, thống kê, và xử lí tín hiệu.
- Scipy giống như Numpy là mã nguồn mở==> sử dụng thoải mái
- Scipy được tạo ra bởi Travis Olliphant, người sáng ra Numpy.

??? Tại sao nên sử dụng Scipy ???(Nếu SciPy sử dụng NumPy ở bên dưới, tại sao chúng ta không thể sử dụng NumPy?
Trả lời: Scipy đã tối ưu hóa và bổ sung các chức năng thường được sử dụng trong Numpy và Data Science.

??? Scipy được viết bằng ngôn ngữ nào ???
Trả lời: Scipy chủ yếu được viết bằng Python, nhưng cũng có một số đoạn được viết bằng C.

??? Cơ sở mã Scipy ở đâu ???
Trả lời: Mã nguồn cho Scipy nằm tại kho lưu github này:  https://github.com/scipy/scipy (Gitbub cho phép nhiều người làm việc trên cùng một cơ sở mã).

$$$ Learning By Reading $$$
- https://www.w3schools.com/python/scipy/scipy_getting_started.php
+) Sơ dồ 10 bài học quan trọng của Scipy:
                   Basic Scipy
       1.        Introduction
       2.        Getting Started
       3.        Constants
       4.        Optimizers(Bộ tối ưu hóa)
       5.        Sparse Data(Dữ liệu thưa thớt)
       6.        Graphs
       7.        Spatial Data(Dữ liệu không gian)
       8.        Matlab Arrays(Mảng Matlab)
       9.        Interpolation(Nội suy)
       10.      Significance Tests


$$$ Import Scipy $$$
- Sau khi Scipy được cài đặt, hãy nhập mô-đun Scipy mà bạn muốn sử dụng trong ứng dụng của mình bằng cách thêm câu lệnh:
       from scipy import constants

+) VÍ DỤ:
from scipy import constants
print(constants.liter)   #nghĩa là 1liter = 0.001 ml
kết quả:   0.001

#Giải thích:
Hằng số:  Scipy cung cấp một tập hợp các hằng số toán học, một trong số đó là   liter   hàm trả về 1 lít dưới dạng mét m=khối.

$$$ Checking Scipy Version $$$
- Chuỗi phiên bản được lưu trữ trong thuộc tính  __version__

+) VÍ DỤ:
import scipy
print(scipy.__version__)
kết quả:   1.13.1      #đây là phiên bản mới nhất tùy vào người dùng download.

!NOTE!:  hai kí tự gạch dưới được sử dụng trong  __version__
 
$$$ Scipy Constants $$$
$$$ Constants in Scipy $$$
- Vì Scipy tập trung nhiều hơn vào các triển khai khoa học nên nó cung cấp nhiều hằng số khoa học tích hợp sẵn.
- Các hằng số này có thể hữu ích khi bạn làm việc với khoa học dữ liệu.
-  PI là một ví dụ về hằng số khoa học.

+) VÍ DỤ: in ra giá trị hằng số PI
from scipy import constants
print(constants.pi)
kết quả:   3.141592653589793

$$$ Constant Units(Đơn vị hằng số) $$$
- Danh sách tất cả các đơn vị trong mô đun hằng số có thể được xem bằng sử dụng hàm    dir()
 
+) VÍ DỤ:
from scipy import constants
print(dir(constants))
kết quả:  ['Avogadro', 'Boltzmann', 'Btu', 'Btu_IT', 'Btu_th', 'C2F', 'C2K', 'ConstantWarning', 'F2C', 'F2K', 'G', 'Julian_year', 'K2C', 'K2F', 'N_A', 'Planck', 'R', 'Rydberg', 'Stefan_Boltzmann', 'Tester', 'Wien', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '_obsolete_constants', 'absolute_import', 'acre', 'alpha', 'angstrom', 'arcmin', 'arcminute', 'arcsec', 'arcsecond', 'astronomical_unit', 'atm', 'atmosphere', 'atomic_mass', 'atto', 'au', 'bar', 'barrel', 'bbl', 'c', 'calorie', 'calorie_IT', 'calorie_th', 'carat', 'centi', 'codata', 'constants', 'convert_temperature', 'day', 'deci', 'degree', 'degree_Fahrenheit', 'deka', 'division', 'dyn', 'dyne', 'e', 'eV', 'electron_mass', 'electron_volt', 'elementary_charge', 'epsilon_0', 'erg', 'exa', 'exbi', 'femto', 'fermi', 'find', 'fine_structure', 'fluid_ounce', 'fluid_ounce_US', 'fluid_ounce_imp', 'foot', 'g', 'gallon', 'gallon_US', 'gallon_imp', 'gas_constant', 'gibi', 'giga', 'golden', 'golden_ratio', 'grain', 'gram', 'gravitational_constant', 'h', 'hbar', 'hectare', 'hecto', 'horsepower', 'hour', 'hp', 'inch', 'k', 'kgf', 'kibi', 'kilo', 'kilogram_force', 'kmh', 'knot', 'lambda2nu', 'lb', 'lbf', 'light_year', 'liter', 'litre', 'long_ton', 'm_e', 'm_n', 'm_p', 'm_u', 'mach', 'mebi', 'mega', 'metric_ton', 'micro', 'micron', 'mil', 'mile', 'milli', 'minute', 'mmHg', 'mph', 'mu_0', 'nano', 'nautical_mile', 'neutron_mass', 'nu2lambda', 'ounce', 'oz', 'parsec', 'pebi', 'peta', 'physical_constants', 'pi', 'pico', 'point', 'pound', 'pound_force', 'precision', 'print_function', 'proton_mass', 'psi', 'pt', 'short_ton', 'sigma', 'speed_of_light', 'speed_of_sound', 'stone', 'survey_foot', 'survey_mile', 'tebi', 'tera', 'test', 'ton_TNT', 'torr', 'troy_ounce', 'troy_pound', 'u', 'unit', 'value', 'week', 'yard', 'year', 'yobi', 'yotta', 'zebi', 'zepto', 'zero_Celsius', 'zetta']

$$$ Unit Categories(Thể loại đơn vị) $$$
- Các đơn vị được sắp xếp vào các danh mục sau:  hệ mét, nhị phân, khối, góc, thời gian, chiều dài, áp lực, âm lượng, tốc độ, nhiệt độ, năng lượng, quyền lực, lực lượng.

$$$ Metric (SI) Prefixes(Tiền tố hệ mét) $$$
- Trả về đơn vị được chỉ định theo mét (ví dụ centi trả về 0.01)

+) VÍ DỤ:
from scipy import constants
print(constants.yotta)
print(constants.zetta)
print(constants.exa)
print(constants.peta)
print(constants.tera)
print(constants.giga)
print(constants.mega)
print(constants.kilo)
print(constants.hecto)
print(constants.deka)
print(constants.deci)
print(constants.centi)
print(constants.milli)
print(constants.micro)
print(constants.nano)
print(constants.pico)
print(constants.femto)
print(constants.atto)
print(constants.zepto)
kết quả:   1e+24
                1e+21
                1e+18
1000000000000000.0
1000000000000.0
        1000000000.0
         1000000.0
             1000.0
               100.0
               10.0
                0.1
               0.01
             0.001
             1e-06
             1e-09
             1e-12
             1e-15
             1e-18
              1e-21

$$$ Binary Prefixes(Tiền tố nhị phân) $$$
- Trả về đơn vị được chỉ định theo byte (ví dụ: kibi trả về 1024)

+) VÍ DỤ:
from scipy import constants
print(constants.kibi)
print(constants.mebi)
print(constants.gibi)
print(constants.tebi)
print(constants.pebi)
print(constants.exbi)
print(constants.zebi)
print(constants.yobi)
kết quả:   1024
              1048576
           1073741824
        1099511627776
     1125899906842624
   1152921504606846976
  1180591620717411303424
1208925819614629174706176

$$$ Mass(khối) $$$
- Trả về đơn vị được chỉ định theo kg (ví dụ gram trả về 0.001).

+) VÍ DỤ:
from scipy import constants
print(constants.gram)
print(constants.metric_ton)
print(constants.grain)
print(constants.lb)
print(constants.pound)
print(constants.oz)
print(constants.ounce)
print(constants.stone)
print(constants.long_ton)
print(constants.short_ton)
print(constants.troy_ounce)
print(constants.troy_pound)
print(constants.carat)
print(constants.atomic_mass)
print(constants.m_u)
print(constants.u)
kết quả:    0.001
                1000.0
            6.479891e-05
    0.45359236999999997
    0.45359236999999997
    0.028349523124999998
    0.028349523124999998
    6.3502931799999995
             1016.0469088
        907.1847399999999
    0.031103476799999998
    0.37324172159999996
                  0.0002
             1.66053904e-27
             1.66053904e-27
             1.66053904e-27

$$$ Angle(Góc) $$$
- Trả về đơn vị được chỉ định theo radian (ví dụ degree trả về 0.017453292519943295).

+) VÍ DỤ:
from scipy import constants
print(constants.degree)
print(constants.acrmin)
print(constants.arcminute)
print(constants.arcsec)
print(constants.arcsecond)
kết quả:   0.017453292519943295
                0.0002908882086657216
                0.0002908882086657216
                4.84813681109536e-06
                4.84813681109536e-06

$$$ Time $$$
- Trả về đơn vị được chỉ định tính bằng giây (ví dụ: hour trả về 3600.0).

+) VÍ DỤ:
from scipy import constants
print(constants.minute)
print(constants.hour)
print(constants.day)
print(constants.week)
print(constants.year)
print(constants.Julian_year)
kết quả:   60.0
              3600.0
             86400.0
            604800.0
           31536000.0
          31557600.0

$$$ Length(Chiều dài) $$$
- Trả về đơn vị được chỉ định theo mét (ví dụ nautical_mile trả về 1852.0).

+) VÍ DỤ:
from scipy import constants
print(constants.inch)
print(constants.foot)
print(constants.yard)
print(constants.mile)
print(constants.mil)
print(constants.pt)
print(constants.point)
print(constants.survey_foot)
print(constants.survey_mile)
print(constants.nautical_mile)
print(constants.fermi)
print(constants.angstrom)
print(constants.au)
print(constants.astronomocal_unit)
print(constants.light_year)
print(constants.parsec)
kết quả:   0.0254
     0.30479999999999996
     0.9143999999999999
     1609.3439999999998
     2.5399999999999997e-05
    0.00035277777777777776
    0.00035277777777777776
   0.3048006096012192
   1609.3472186944373
                1852.0
                1e-15
                1e-10
                1e-06
           149597870691.0
           149597870691.0
          9460730472580800.0
       3.0856775813057292e+1

$$$ Pressure(Áp lực) $$$
- Trả về đơn vị được chỉ định theo pascal (ví dụ psi trả về 6894.757293168361).

+) VÍ DỤ:
from scipy import constants
print(constants.atm)
print(constants.atmosphere)
print(constants.bar)
print(constants.torr)
print(constants.mmHg)
print(constants.psi)
kết quả:   101325.0
                101325.0
               100000.0
   133.32236842105263
   133.32236842105263
   6894.757293168361

$$$ Area(Khu vực) $$$
- Trả về đơn vị được chỉ định theo mét vuông (ví dụ hectare trả về 10000.0).

+) VÍ DỤ:
from scipy import constants
print(constants.hectare)
print(constants.acre)
kết quả:    10000.0
          4046.8564223999992

$$$ Volume(Âm lượng) $$$
- Trả về đơn vị được chỉ định theo mét khối (ví dụ liter trả về  0.001).

+) VÍ DỤ:
from scipy import constants
print(constants.liter)
print(constants.litre)
print(constants.gallon)
print(constants.gallon_US)
print(constants.gallon_imp)
print(constants.fluid_ounce)
print(constants.fluid_ounce_US)
print(constants.fluid_ounce_imp)
print(constants.barrel)
print(constants.bbl)
kết quả:    0.001
                 0.001
  0.0037854117839999997
  0.0037854117839999997
  0.00454609
  2.9573529562499998e-05
  2.9573529562499998e-05
  2.84130625e-05
  0.15898729492799998
  0.15898729492799998

$$$ Speed(Tốc độ) $$$ 
- Trả đơn vị được chỉ định theo mét trên giây (ví speed_of_sound trả về 340.5).

+) VÍ DỤ:
from scipy import constants
print(constants.kmh)
print(constants.mph)
print(constants.mach)
print(constants.speed_of_sound)
print(constants.knot)
kết quả:  0.001
               0.001
0.0037854117839999997
0.0037854117839999997
          0.00454609
2.9573529562499998e-05
2.9573529562499998e-05
2.84130625e-05
0.15898729492799998
0.15898729492799998

$$$ Temperature(Nhiệt độ) $$$
- Trả về đơn vị được chỉ định theo Kelvin (ví dụ zero_Celsius trả về 273.15).

+) VÍ DỤ:
from scipy import constants
print(constants.zero_Celsius)
print(constants.degree_Fahrenheit)
kết quả:  273.15
    0.5555555555555556

$$$ Energy(Năng lượng) $$$
- Trả về đơn vị được chỉ định theo joule (ví dụ calorie trả về 4.184).

+) VÍ DỤ:
from scipy import constants
print(constants.eV)
print(constants.electron_volt)
print(constants.calorie)
print(constants.calorie_th)
print(constants.calorie_IT)
print(constants.erg)
print(constants.Btu)
print(constants.Btu_IT)
print(constants.Btu_th)
print(constants.Btu_TNT)
kết quả:   1.6021766208e-19
                1.6021766208e-19
                       4.184
                       4.184
                      4.1868
                        1e-07
             1055.05585262
             1055.05585262
          1054.3502644888888
               4184000000.0

$$$ Power(Quyền lực) $$$
- Trả về đơn vị được chỉ định theo watt (ví dụ horsepower trả về 745.6998715822701).

+) VÍ DỤ:
from scipy import constants
print(constants.hp)
print(constants.horsepower)
kết quả:   745.6998715822701
                745.6998715822701

$$$ Force(Lực lượng) $$$
- Trả về đơn vị được chỉ định theo Newton (ví dụ kilogram_force trả về 9.80665).

+) VÍ DỤ:
from scipy import constants
print(constants.dyn)
print(constants.dyne)
print(constants.lbf)
print(constants.pound_force)
print(constants.kgf)
print(constants.kilogram_force)
kết quả:    1e-05
                  1e-05
     4.4482216152605
     4.4482216152605
                9.80665
                9.80665

$$$ Scipy Optimizers(Bộ tối ưu hóa) $$$
- Trình tối ưu hóa là một tập hợp các quy trình được định nghĩa trong Scipy để tìm giá trị nhỏ nhất của một hàm hoặc một nghiệm của một phương trình.

$$$ Optimizing in Functions(Tối ưu hóa các hàm) $$$
- Về cơ bản, tất cả các thuật toán trong Machine Learning đều không có gì hơn là một phương trình phức tạp cần được tối thiểu hóa với sự trợ giúp của dữ liệu cho sẵn.

$$$ Roots of an Equation(Căn của một phương trình) $$$
+) Numpy có khả năng tìm nghiệm cho đa thức và phương trình tuyến tính, nhưng không thể tìm nghiệm cho phương phi tuyến tính, như phương trình này:
         x +cos(x)
- Bạn có thể sử dụng chức năng   optimize.root   của Scipy để thực hiện việc đó.
+) Hàm này cần có hai số đối bắt buộc:
       fun - một hàm biển diễn một phương trình.
       x0 - dự đoán ban đầu cho căn bậc hai.
- Hàm này trả về một đối tượng có thông tin liên quan đến giải pháp.
+) Giải pháp thực tế được đưa ra dưới thuộc tính    x   của đối tượng trả về:

+) VÍ DỤ: Tìm nghiệm của phương trình x + cos(x)
from scipy.optimize import root
from math import cos
def eqn(x):
myroot = root(eqn, 0)
print(myroot.x)
kết quả:   [-0.73908513]

!NOTE!:  Đối tượng trả về có nhiều thông tin hơn về giải pháp.

+) VÍ DỤ khác: in tất cả thông tin về giải pháp (không chỉ   x   thông tin về gốc)
from scipy.optimize import root
from math import cos
def eqn(x):
myroot = root(eqn, 0)
print(myroot)
kết quả:     fjac: array([[-1.]])
     fun: array([ 0.])
 message: 'The solution converged.'
    nfev: 9
     qtf: array([ -2.66786593e-13])
       r: array([-1.67361202])
  status: 1
 success: True
       x: array([-0.73908513])

$$$ Minimizing a Function(Tối thiểu hóa một hàm) $$$
- Trong bối cảnh này, hàm số biểu diễn một đường cong, đường cong có điểm cao nhất và điểm thấp nhất .
     Điểm cao nhất được gọi là cực đại.
     Điểm thấp nhất được gọi là cực tiểu.
     Điểm cao nhất trên toàn bộ đường cong được gọi là cực đại toàn cục , trong khi phần còn lại được gọi là cực đại cục bộ.
     Điểm thấp nhất trong toàn bộ đường cong được gọi là cực tiểu toàn cục , trong khi phần còn lại được gọi là cực tiểu cục bộ .

$$$ Finding Minima $$$
- Chúng ta có thể sử dụng hàm    scipy.optimize.minimize()    để thu gọn hàm.   
+) Hàm    minimize()    có các đối số sau:
       fun - một hàm biểu diễn một phương trình.
       x0 - dự đoán ban đầu cho căn bậc hai.
+) method - tên của phương pháp sử dụng. Giá trị pháp lý:
         'CG'
         'BFGS'
         'Newton-CG'
         'L-BFGS-B'
         'TNC'
         'COBYLA'
         'SLSQP'
+) callback- hàm được gọi sau mỗi lần lặp lại của quá trình tối ưu hóa.
+) options - một từ điển định nghĩa các tham số bổ sung:
      {
              "disp": boolean - print detailed description
              "gtol": number - the tolerance of the error
      }

+) VÍ DỤ: thu nhỏ hàm x^2 + x + 2 bằng BFGS:
from scipy.optimize import minimize
def eqn(x):
   return x**2 + x + 2
mymin = minimize(eqn, 0, method ="BFGS")
print(mymin)
kết quả:   message: Optimization terminated successfully.
                success: True
                 status: 0
                     fun: 1.75
                        x: [-5.000e-01]
                     nit: 2
                     jac: [ 0.000e+00]
            hess_inv: [[ 5.000e-01]]
                     nfev: 8
                     njev: 4

$$$ Scipy Sparse Data(Dữ liệu thưa thớt) $$$
$$$ What is sparse data?
- Dữ liệu thưa thớt là dữ liệu có nhiều phần tử chưa được sử dụng (phần tử không mang bất kì thông tin nào).
+) Nó có thể là một mảng như thế này:   [1, 0, 2, 0, 0, 3, 0, 0, 0, 0, 0, 0]
- Dữ liệu thưa thớt: là tập dữ liệu mà hầu hết các giá trị mục bằng 0.
- Mảng dày đặc: ngược lại với mảng thưa: hầu hết các giá trị không bằng 0.
(Trong khoa học tính toán, khi chúng ta xử lý đạo hàm riêng trong đại số tuyến tính, chúng ta sẽ gặp dữ liệu thưa thớt.)

$$$ How to Work With Sparse Data $$$
- Scipy có một mô-đun    scipy.sparse    cung cấp các hàm để xử lí dữ liệu thưa thớt.
+) Về cơ bản, có hai loại ma trận thưa thớt mà chúng ta sử dụng:
        CSC - Compressed Sparse Column(Cột thưa nén) - Để tính toán hiểu quả, cắt cột nhanh.
        CSR - Compressed Sparse Row(Hàng thưa nén) - Để cắt hàng nhanh, tích vectơ ma trận nhanh hơn.
==> Chúng tôi sẽ sử dụng ma trận CSR trong hướng dẫn này.

$$$ CSR Matrix $$$
- Chúng ta có thể tạo ma trận CSR bằng cách truyền một mảng vào hàm    scipy.sparse.csr_matrix()        .

+) VÍ DỤ: Tạo ma trận CSR từ một mảng:
import numpy as np
from scipy.sparse import csr_matrix
arr = np.array([0, 0, 0, 0, 0, 1, 1, 0, 2])
print(csr_matrix(arr))
kết quả:   (0, 5)	1
                (0, 6)	1
                (0, 8)	2

#Giải thích:
    Từ kết quả ta thấy có 3 mục có giá trị:
    Mục 1. nằm ở 0 vị trí hàng 5 và có giá trị 1.
    Mục 2. nằm ở 0 vị trí hàng 6 và có giá trị 1.
    Mục 3. nằm ở 0 vị trí hàng 8 và có giá trị 2.

$$$ Sparse Matrix Methods(Phương pháp ma trận thưa thớt) $$$
- Xem dữ liệu được lưu trữ (không phải các mục số 0) bằng thuộc tính    data     :

+) VÍ DỤ:
import numpy as np
from scipy.sparse import csr_matrix
arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
print(csr_matrix(arr).data)
kết quả:    [1 1 2]

- Đếm các số khác không bằng phương pháp    count_nonzero()     :

+) VÍ DỤ:
import numpy as np
from scipy.sparse import csr_matrix
arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
print(csr_matrix(arr).count_nonzero())
kết quả:    3

- Loại bỏ các phần tử bằng 0 khỏi ma trận bằng phương pháp     eliminate_zeros()      :
 
+) VÍ DỤ:
import numpy as np
from scipy.sprase import csr_matrix
arr = np.array([[0,0,0], [0,0,1], [1,0,2]])
mat  = csr_matrix(arr)
mat.eliminate_zeros()
print(mat)                     #nếu dùng cách này  print(csr_matrix(arr).eliminate_zeros()) thì kết quả bị khác, nó ra là None.
kết quả:  (1, 2)	1
               (2, 0)	1
               (2, 2)	2

- Loại bỏ các mục trùng lặp bằng phương pháp     sum_duplicates()             :

+) VÍ DỤ:
import numpy as np
from scipy.sparse import csr_matrix
arr = np.array([[0,0,0], [0,0,1], [1,0,2]])
mat = csr_matrix(arr)
mat = sum_duplicates()
print(mat)                       #nếu dùng cách này print(csr_matrix(arr).sum_duplicates()) thì kết quả bị khác, nó ra là None.
kết quả:       (1, 2)	1
                    (2, 0)	1
                     (2, 2)	2

- Chuyển đổi từ csr sang csc bằng phương pháp      tocsc()              :

+) VÍ DỤ:
import numpy as np
from scipy.sparse import csr_matrix
arr = np.array([[0,0,0], [0,0,1], [1,0,2]])
newarr = csr_matrix(arr).tocsc()
print(newarr)
kết quả:     (2, 0)	1
                  (1, 2)	1
                  (2, 2)	2

!NOTE!:  Ngoài các phép toán cụ thể thưa thớt đã đề cập, ma trận thưa thớt hỗ trợ tất cả các phép toán mà ma trận thông thường hỗ trợ, ví dụ như định hình lại, tính tổng, số học, phát sóng, v.v.

$$$ Scipy Graphs $$$
$$$ Working with Graphs $$$
- Đồ thị là một cấu trúc dữ liệu thiết yếu.
- Scipy cung cấp cho chung ta mô đun    scipy.sparse.csgraph     để làm việc với các cấu trúc dữ liệu như vậy.

$$$ Adjacency Matrix(Ma trận kề) $$$
- Ma trận kề là ma trận     nxn      biểu diễn    n    số phần tử trong một đồ thị.
- và các giá trị thể hiện mối liên hệ giữa các yếu tố.

+) VÍ DỤ:    https://www.w3schools.com/python/scipy_graph.png
#Giải thích:
    Đối với đồ thị như thế này, với các phần tử A,B, và C các kết nối là:
       A và B được kết nối với trọng số 1.
       A và C được kết nối với trọng số 2.
       C và B không được kết nối.
Ma trận liên quan sẽ trông như thế này:      ABC 
                                                                  A:[0 1 2]   
                                                                  B:[1 0 0] 
                                                                  C:[2 0 0]

$$$ Connected Components(Các thành phần được kết nối) $$$
- Tìm tất cả các thành phần được kết nối bằng phương pháp   connected_components()        .

+) VÍ DỤ:
import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix
arr = np.array([
   [0,1,2],
   [1,0,0],
   [2,0,0]
])
newarr = csr_matrix(arr)
print(connected_components(newarr))
kết quả:   (1, array([0, 0, 0], dtype=int32))

$$$ Dijkstra $$$
- Sử dụng phương pháp    dijkstra     này để tìm đường đi ngắn nhất trong đồ thị từ phần tử này đến phần tử khác.
+) Cần những lập luận sau:
    1. return_predecessors: boolean (True để trả về toàn bộ đường dẫn duyệt, nếu không thì trả về False).
    2. indices(chỉ mục): chỉ mục của phần tử để trả về tất cả các đường dẫn chỉ từ phần tử đó.
    3. limit(giới hạn): trọng lượng tối đa của đường dẫn.

+) VÍ DỤ:
import numpy as np
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix
arr = np.array([
    [0,1,2],
    [1,0,0],
    [2,0,0]
])
newarr = csr_matrix(arr)
print(dijkstra(newarr, return_Predecessors=True, indices=0))
kết quả:  (array([ 0.,  1.,  2.]), array([-9999,     0,     0], dtype=int32))

$$$ Floyd Warshall $$$
- Sử dụng phương pháp    floyd_warshall()      này để tìm đường đi ngắn nhất giữa các cặp phần tử.

+) VÍ DỤ:
import numpy as np
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix
arr = np.array ([
   [0,1,2],
   [1,0,0],
   [2,0,0]
])
print(floyd_warshall(newarr, return_predecessors=True))
kết quả:   (array([[ 0.,  1.,  2.],
       [ 1.,  0.,  3.],
       [ 2.,  3.,  0.]]), array([[-9999,     0,     0],
       [    1, -9999,     0],
       [    2,     0, -9999]], dtype=int32))

$$$ Bellman Ford $$$
- Phương pháp này    bellman_ford()     cũng có thể tìm ra đường đi ngắn nhất giữa tất cả các cặp phần tử, nhưng phương pháp này cũng có thể xử lý được trọng số âm.

+) VÍ DỤ:
import numpy as np
from scipy.sparse.csgraph import bellman_ford
from scipy.sparse import csr_matrix
arr = np.array ([
   [0,-1,2],
   [1,0,0],
   [2,0,0]
])
newarr = csr_matrix(arr)
print(bellman_ford(newarr, return_predecessors=True, indices=0))
kết quả:  (array([ 0., -1.,  2.]), array([-9999,     0,     0], dtype=int32))

$$$ Depth First Order(Độ sâu bậc nhất) $$$
- Phương pháp này    depth_first_order()      trả về phép duyệt theo chiều sâu từ một nút.
+) Hàm này có các đối số sau:
    1. Đồ thị
    2. Phần tử bắt đầu để duyệt đồ thị.

+) VÍ DỤ:
import numpy as np
from scipy.sparse.csgraph import depth_first_order
from scipy.sparse import csr_matrix
arr = np.array ([ 
  [0,1,0,1],
  [1,1,1,1],
  [2,1,1,0],
  [0,1,0,1]
])
newarr = csr_matrix(arr)
print(depth_first_order(newarr, 1))
kết quả:  (array([1, 0, 3, 2], dtype=int32), array([    1, -9999,     1,     0], dtype=int32))

$$$ Breadth First Order $$$
- Phương pháp này    breadth_first_order()     trả về phép duyệt theo chiều rộng từ một nút.
+) Hàm này có các đối số sau:
   1. Đồ thị.
   2. Phần tử bắt đầu để duyệt đồ thị.

+) VÍ DỤ:
import numpy as np
from scipy.sparse.csgraph import breadth_first_order
from scipy.sparse import csr_matrix
arr = np.array ([
  [0,1,0,1],
  [1,1,1,1], 
  [2,1,1,0],
  [0,1,0,1]
])
newarr = csr_matrix(arr)
print(breadth_first_order(newarr, 1))
kết quả:   (array([1, 0, 2, 3], dtype=int32), array([    1, -9999,     1,     1], dtype=int32))

$$$ Scipy Spatial Data(Dữ liệu không gian) $$$
- Dữ liệu không gian là dữ liệu được biểu diễn trong không gian hình học.
- Ví dụ các điểm trên một hệ tọa độ.
- Chúng tôi xử lý các vấn đề về dữ liệu không gian trong nhiều nhiệm vụ.
Ví dụ tìm xem một điểm có nằm trong ranh giới hay không.
- SciPy cung cấp cho chúng ta mô-đun scipy.spatialcó các chức năng để làm việc với dữ liệu không gian.

$$$ Triangulation(Tam giá hóa) $$$
- Phép chia tam giác một đa giác là chia đa giác đó thành nhiều tam giác mà ta có thể tính được diện tích của đa giác đó.
- Phép tam giác hóa với các điểm có nghĩa là tạo ra các tam giác được tạo thành trên bề mặt trong đó tất cả các điểm đã cho đều nằm trên ít nhất một đỉnh của bất kỳ tam giác nào trên bề mặt.
- Một phương pháp để tạo ra các phép tam giác hóa thông qua các điểm là      Delaunay()      phép tam giác hóa.

+) VÍ DỤ:
#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

import numpy as np
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt
points = np.array([
   [2,4],
   [3,4],
   [3,0],
   [2,2],
   [4,1]
])
simplices = Delaunay(points).simplices
plt.triplot(points[:, 0], points[:, 1], simplices)
plt.scatter(points[:, 0], points[:, 1], color="r")
plt.show()
#two lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
kết quả:    https://www.w3schools.com/python/scipy_spatial_delaunay.png

!NOTE!:  Thuộc tính này  simplices   tạo ra sự tổng quát của ký hiểu tam giác.

$$$ Convex Hull(Vỏ lồi) $$$
- Một lớp vỏ lồi là đa giác nhỏ nhất bao phủ tất cả các điểm đã cho.
- Sử dụng phương pháp     ConvexHull()       để tạo ra một Convex Hull.

+) VÍ DỤ:
#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt
points = np.array ([
   [2,4],
  [3, 4],
  [3, 0],
  [2, 2],
  [4, 1],
  [1, 2],
  [5, 0],
  [3, 1],
  [1, 2],
  [0, 2]
])
hull = ConvexHull(points)
hull_points = hull.simplices
plt.scatter(points[:, 0], points[:, 1])
for simplex in hull_points:
  plt.plot(points[simplex,0], points[simplex,1], 'k-')
plt.show()
#Two lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
kết quả:    https://www.w3schools.com/python/scipy_spatial_convexhull.png

$$$ KDTree $$$
- KDTrees là một cấu trúc dữ liệu được tối ưu hóa cho các truy vấn tìm kiếm hàng xóm gần nhất.
Ví dụ, trong một tập hợp các điểm sử dụng KDTrees, chúng ta có thể hỏi hiệu quả những điểm nào gần nhất với một điểm nhất định nào đó.
- Phương pháp      KDTree()     trả về một đối tượng KDTree.
- Phương pháp       query()          trả về khoảng cách đến hàng xóm gần nhất và vị trị của hàng xóm.

+) VÍ DỤ:
from scipy.spatial import KDTree
points = [(1,-1), (2,3), (-2,3), (2,-3)]
kdtree = KDTree(points)
res = kdtree.query((1,1))                   #res viết tắt từ result
print(res)
kết quả:   (2.0, 0)

$$$ Distance Matrix(Ma trận khoảng cách) $$$
- Có nhiều Chỉ số khoảng cách được sử dụng để tìm các loại khoảng cách khác nhau giữa hai điểm trong khoa học dữ liệu, khoảng cách Euclid, khoảng cách cosin, v.v.
- Khoảng cách giữa hai vectơ không chỉ là độ dài của đường thẳng nối chúng mà còn có thể là góc giữa chúng tính từ gốc tọa độ hoặc số bước đơn vị cần thiết, v.v.
- Hiệu suất của nhiều thuật toán Machine Learning phụ thuộc rất nhiều vào số liệu khoảng cách. Ví dụ "K Nearest Neighbors" hoặc "K Means" v.v.

+) VÍ DỤ:
from scipy.spatial.distance import euclidean
p1 = (1,0)
p2 = (10, 2)
res = euclidean(p1,p2)                       #res viết tắt từ result
print(res)
kết quả:   9.21954445729

$$$ Cityblock Distance (Manhattan Distance)(Khoảng cách Manhattan) $$$
- Khoảng cách được tính bằng cách sử dụng 4 độ chuyển động.
- Ví dụ chúng ta chỉ có thể di chuyển: lên, xuống, sang phải hoặc sang trái, không thể di chuyển theo đường chéo.

+) VÍ DỤ:
froom scipy.spatial.distance import cityblock
p1 = (1,0)
p2 = (10,2)
res = cityblock(p1, p2)                       #res viết tắt từ result
print(res)
kết quả:  11

$$$ Cosine Distance(Khoảng cách Cosin) $$$
- Là giá trị của góc cosin giữa hai điểm A và B.

+) VÍ DỤ:
from scipy.spatial.distance import cosine
p1 = (1,0)
p2 = (10,2)
res = cosine(p1, p2)                               #res viết tắt từ result
print(res)
kết quả:    0.0194193243091

$$$ Hamming Distance(Khoảng cách Hamming) $$$
- Là tỷ lệ bit trong đó có hai bit khác nhau.
- Đây là cách đo khoảng cách cho chuỗi nhị phân.

VÍ DỤ:
from scipy.spatial.distance import hamming
p1 = (True, False, True)
p2 = (False, True, True)
res = hamming(p1, p2)                               #res viết tắt từ result
print(res)
kết quả:    0.666666666667

$$$ Scipy Matlab Arrays $$$
$$$ Working With Matlab Arrays $$$
- Scipy cung cấp cho chúng ta mô-đun    scipy.io     có các chức năng để làm việc với mảng Matlab.

$$$ Extracting Data in Matlab format(Xuất dữ liệu theo định dạng Matlab) $$$
- Chức năng     savemat()     cho phép chúng ta xuất dữ liệu theo định dạng Matlab.
+) Phương pháp này sử dụng các tham số sau:
   1. filename - tên tệp để lưu dữ liệu.
   2. mdict - một từ điển chứa dữ liệu.
   3. do_compression - giá trị boolean chỉ định có nén kết quả hay không. Mặc định là False.

+) VÍ DỤ:
from scipy import io                  #io viết tắt là  input/output.
import numpy as np
arr = np.arange(10)
io.savemat('arr.mat', {"vec": arr})

!NOTE!: Ví dụ  
from scipy import io                   #io viết tắt là  input/output.
import numpy as np
arr = np.arange(10)
iso.savemat('arr.mat', {"vec": arr})

!NOTE!:  Ví dụ trên sẽ lưu tệp có tên "arr.mat" trên máy tính của bạn. Để mở tệp, hãy xem ví dụ "Nhập dữ liệu từ định dạng Matlab" bên dưới:

$$$ Import Data from Matlab Format(Nhập dữ liệu từ định định dạng Matlab) $$$
- Hàm     loadmat()     cho phép chúng ta nhập dữ liệu từ tệp Matlab.
+) Hàm này có một tham số bắt buộc:
filename - tên tệp của dữ liệu đã lưu.
- Nó sẽ trả về một mảng có cấu trúc trong đó các khóa là tên biến và các giá trị tương ứng với giá trị biến.

+) VÍ DỤ:
from scipy import io                                    #io viết tắt là  input/output.
import numpy as np
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
#Export:
io.savemat('arr.mat', {"vec": arr})
#import:
mydata = io.loadmat('arr.mat')
print(mydata)
kết quả:   {
  '__header__': b'MATLAB 5.0 MAT-file Platform: nt, Created on: Tue Sep 22 13:12:32 2020',
  '__version__': '1.0',
  '__globals__': [],
  'vec': array([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]])
}

- Sử dụng tên biến "vec" để chỉ hiển thị mảng từ dữ liệu matlab:
+) VÍ DỤ:
...
print(mydata['vec'])          #vec viết tắt là vector.
kết quả: [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]

!NOTE!:  Ta có thể thấy mảng ban đầu là một chiều, nhưng khi trích xuất nó đã tăng thêm một chiều.
+) Để giải quyết vấn đề này, chúng ta có thể truyền thêm một đối số       squeeze_me=True       :

+) VÍ DỤ
from scipy import  io                                    #io viết tắt là  input/output.
import numpy as np
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
#Export:
io.savemat('arr.mat', {"vec": arr})              #vec viết tắt là vector.
#Import:
mydata = io.loadmat('arr.mat', squeeze_me=True)
print(mydata['vec'])
kết quả: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

$$$ Scipy Interpolation(Nội suy) $$$
$$$ What is interpolation? $$$
- Nội suy là phương pháp tạo ra các điểm giữa các diểm cho trước.
- Ví dụ đối với điểm 1 và 2, chúng ta có thể nội suy và tìm ra điểm 1,33 và 1,66.
- Nội suy có nhiều ứng dụng, trong Học máy, chúng ta thường xử lý dữ liệu bị thiếu trong một tập dữ liệu, nội suy thường được sử dụng để thay thế các giá trị đó.
- Phương pháp điền giá trị này được gọi là imputation(sự quy kết).
- Ngoài việc imputation(sự quy kết), nội suy thường được sử dụng khi chúng ta cần làm mịn các điểm rời rạc trong một tập dữ liệu.

$$$ How to implement it in Scipy(Làm thế nào để triển khai nó trong Scipy) $$$
+) Scipy cung cấp cho chúng ta một mô đun có tên là     scipy.interpolate()     có nhiều chức năng để sử lí nội suy:

$$$ 1D Interpolation(Nội suy 1D) $$$
- Hàm này    interp1d()     được sử dụng để nội suy một phân phối có 1 biến.
- Nó lấy x và y trỏ và trả về một hàm có thể gọi được với new x và trả về y.
    
+) VÍ DỤ:
from scipy.interpolate import interp1d
import numpy as np
xs = np.arange(10)
ys = 2*xs + 1
interp_func = interp1d(xs, ys)
newarr = interp_func(np.arange(2.1, 3, 0.1))
print(newarr)
kết quả:    [ 5.2  5.4  5.6  5.8  6.   6.2  6.4  6.6  6.8]

!NOTE!:  giá trị xs mới phải nằm cùng phạm với giá trị xs cũ, nghĩa là chúng ta không thể gọi   interp_func()    với giá trị cao hơn 10 hoặc nhỏ hơn 0.

$$$ Spline Interpolation( Nội suy Spline) $$$
- Trong nội suy 1D, các điểm được khớp với một đường cong đơn trong khi trong nội suy Spline, các điểm được khớp với một hàm từng phần được xác định bằng đa thức gọi là spline.
- Hàm    UnivariateSpline()      lấy xs và ys tạo ra một hàm có thể gọi được bằng lệnh new xs.
- Hàm từng phần:  Một hàm có định nghĩa khác nhau cho các phạm vi khác nhau.

+) VÍ DỤ:
from scipy.interpolate import UnivariateSpline
import numpy as np
xs = np.arange(10)
ys = xs**2 + np.sin(xs) + 1
interp_func = UnivariateSpline(xs, ys)
newarr = interp_func(np.arange(2.1, 3, 0.1))
print(newarr)
kết quả:  [5.62826474 6.03987348 6.47131994 6.92265019 7.3939103  7.88514634
 8.39640439 8.92773053 9.47917082]

$$$ Interpolation with Radial Basis Function(Nội suy với hàm cơ sở bán kính) $$$
- Hàm cơ sở hướng tâm là hàm được định nghĩa tương ứng với một điểm tham chiếu cố định.
- Hàm     Rbf()    cũng lấy xs và ys làm đối số và tạo ra một hàm có thể gọi được bằng lệnh new xs.

+) VÍ DỤ: (Nội suy các xs và ys sau bằng cách sử dụng rbf và tìm giá trị cho 2.1, 2.2 ... 2.9)
from scipy.interpolate import Rbf
import numpy as np
xs = np.arange(10)
ys = xs**2+np.sin(xs) + 1
interp_func = Rbf(xs, ys)
newarr = interp_func(np.arange(2.1, 3, 0.1))
print(newarr)
kết quả:   [ 6.25748981  6.62190817  7.00310702  7.40121814  7.8161443   8.24773402
                8.69590519  9.16070828  9.64233874]

$$$ Scipy Statistical Significance Tests(Kiểm tra ý nghĩa thông kê) $$$
- Trong thống kê, ý nghĩa thống kê có nghĩa là kết quả được đưa ra phải có lý do đằng sau, chứ không phải được đưa ra một cách ngẫu nhiên hay tình cờ.
- SciPy cung cấp cho chúng ta một mô-đun có tên là       scipy.stats       , có các chức năng thực hiện các thử nghiệm ý nghĩa thống kê.

$$$ Hypothesis of Statistics(Giả thuyết trong thống kê) $$$
-  Giả thuyết là một giả định về một tham số trong quần thể.
$$$ Null Hypothesis $$$
- Nó giả định rằng quan sát này không có ý nghĩa thống kê.
$$$ Alternate Hypothesis $$$
- Nó cho rằng những quan sát đó là do một lý do nào đó.
- Nó thay thế cho Giả thuyết Null.
Ví dụ: Để đánh giá một học sinh chúng ta sẽ thực hiện:
"học sinh tệ hơn mức trung bình" - như một giả thuyết vô hiệu, và:
'học sinh giỏi hơn mức trung bình" - như một giả thuyết thay thế.

$$$ One Tailed Test(Kiểm tra một đuôi) $$$
- Khi giả thuyết của chúng ta chỉ kiểm tra một phía của giá trị, thì nó được gọi là "kiểm tra một đuôi".
Ví dụ: Đối với giả thuyết không:
"giá trị trung bình bằng k", chúng ta có thể có giả thuyết thay thế:
"giá trị trung bình nhỏ hơn k", hoặc:
"giá trị trung bình lớn hơn k"

$$$ Two Tailed Test $$$
- Khi giả thuyết của chúng ta được kiểm định ở cả hai vế của giá trị:
Ví dụ: Đối với giả thuyết không:
"giá trị trung bình bằng k", chúng ta có thể có giả thuyết thay thế:
"giá trị trung bình không bằng k"
=> Trong trường hợp này, giá trị trung bình nhỏ hơn hoặc lớn hơn k và cả hai vế đều cần được kiểm tra.
 
$$$ Alpha Value(Giá trị Alpha) $$$
- Giá trị Alpha là mức độ có ý nghĩa.
Ví dụ: 
Dữ liệu phải gần với giá trị cực đại đến mức nào để giả thuyết vô hiệu bị bác bỏ.
Thông thường được lấy là 0,01, 0,05 hoặc 0,1.

$$$ P Value $$$
- Giá trị P cho biết dữ liệu thực sự gần với giá trị cực đại đến mức nào.
Giá trị P và giá trị Alpha được so sánh để xác định ý nghĩa thống kê.
Nếu giá trị p <= alpha, chúng ta bác bỏ giả thuyết không và nói rằng dữ liệu có ý nghĩa thống kê. Nếu không, chúng ta chấp nhận giả thuyết không.

$$$ T-Test(Kiểm định T) $$$
- Kiểm định T được sử dụng để xác định xem có sự khác biệt đáng kể nào giữa giá trị trung bình của hai biến hay không và cho chúng ta biết liệu chúng có thuộc cùng một phân phối hay không.
- Đây là bài kiểm tra hai đuôi.
- Hàm     ttest_ind()    lấy hai mẫu có cùng kích thước và tạo ra một bộ thống kê t và giá trị p.

+) VÍ DỤ: (Tìm xem các giá trị v1 và v2 đã cho có cùng phân phối hay không)
import numpy as np
from scipy.stats import ttest_ind
v1 = np.random.normal(size=100)
v2 = np.random.normal(size=100)
res = ttest_ind(v1,v2)
print(res)
kết quả:  Ttest_indResult(statistic=0.88243958372222664, pvalue=0.37860920117232288)

- Nếu bạn chỉ muốn trả về giá trị p, hãy sử dụng thuộc tính       pvalue        :
VÍ DỤ:
import numpy as np
from scipy.stats import ttest_ind
v1 = np.random.normal(size = 150)
v2 = np.random.normal(size = 150)
res = ttest_ind(v1,v2). pvalue
print(res)
kết quả:  0.25620998279625834

$$$ KS-Test $$$
- Kiểm định KS được sử dụng để kiểm tra xem các giá trị cho trước có tuân theo phân phối hay không.
- Hàm này lấy giá trị cần kiểm tra và CDF làm hai tham số.
(CDF có thể là một chuỗi hoặc một hàm số có thể gọi trả về xác xuất).
- Có thể sử dụng như một bài kiểm tra một đuôi hoặc hai đuôi.
- Theo mặc định, nó là hai đuôi. Chúng ta có thể truyền tham số alternative dưới dạng một chuỗi có một trong hai đuôi, ít hơn hoặc lớn hơn.

+) VÍ DỤ:
import  numpy as np
from scipy.stats import kstest
v = np.random.normal(size = 100)
res = kstest(v, "norm")
print(res)
kết quả:  KstestResult(statistic=0.084401539828641625, pvalue=0.45521368177068711)

$$$ Statistical Description of Data(Mô tả thống kê dữ liệu) $$$
- Để xem tóm tắt các giá trị trong một mảng, chúng ta có thể sử dụng hàm       describe()         :
+) Nó trả về mô tả sau:
   1. số lượng quan sát(nobs) 
   2. giá trị tối thiểu và tối đa = minmax
   3. mean
   4. sự khác biệt(variance)
   5. sự lệch(skewness)
   6. độ nhọn(kurtosis)

+) VÍ DỤ:
import numpy as np
from scipy.stats import describe
v = np.random.normal(size=100)
res = describe(v)
print(res)
kết quả:  DescribeResult(nobs=100, minmax=(-2.3619583476726906, 3.6013415966325271), mean=0.024135778096377618, variance=1.0256595282420293, skewness=0.3930334975486432, kurtosis=0.6156205017992389)

$$$ Normality Tests (Skewness and Kurtosis)(Kiểm tra tính chuẩn(Độ lệch và Độ nhọn) $$$
- Kiểm tra tính chuẩn dự trên độ lệch và độ nhọn.
Hàm     normaltest()     trả về giá trị p cho giả thuyết null:
"x xuất phát từ phân phối chuẩn".

$$$ Độ Lệch $$$
- Một thước đo tính đối xứng trong dữ liệu.
- Đối với phân phối chuẩn thì bằng 0.
  -   Nếu giá trị âm, nghĩa là dữ liệu bị lệch về bên trái.
  -   Nếu dương thì có nghĩa là dữ liệu bị lệch sang phải.

$$$ Độ Nhọn $$$
- Một thước đo cho biết dữ liệu có phân phối chuẩn chặt chẽ hay nhẹ nhàng.
- Độ nhọn dương có nghĩa là đuôi nặng.
- Độ nhọn âm có nghĩa là đuôi nhẹ.

+) VÍ DỤ: Tìm độ lệch và độ nhọn của các giá trị trong một mảng:
import numpy as np
from scipy.stats import skew kurtosis
v = np.random.normal(size = 100)
print(skew(v))
print(kurtosis(v))
kết quả:    0.057154289489975044
                -0.22658037009318877

+) VÍ DỤ: Tìm xem dữ liệu có xuất phát từ phân phối chuẩn hay không:
import numpy as np
from scipy.stats import normaltest
v  = np.random.normal(size = 100)
print(normaltest(v))
kết quả:   NormaltestResult(statistic=2.588104051559865, pvalue=0.2741576355545209)

___________________________________________________________________________________________Hết_____________________________________________________________________________________________________________________

















