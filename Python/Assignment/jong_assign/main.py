import os
import glob
import re
import matplotlib.pyplot as plt
from shapely.geometry import LineString
import math
import numpy as np
import time
import pandas as pd

# x와 y에 해당하는 그래프의 numpy array를 넘겨주면 We can get the area under the curve.
def get_area(xx, yy):
    return np.trapz(x=xx, y=yy, dx=0.1)

# .out 파일의 내용물을 읽어들이기 위한 함수        
# cen은 .out 파일에서 얻고자 하는 열이다. 인덱스는 0부터 시작하므로 cen-1을 이용해서 사용 즉, 예를 들어 2열을 얻고 싶으면 cen-1에 의해서 그 결과는 1이다.
def read_file(path, cen):
    j = np.array([])

    with open(path) as file:
        for test in file:
            j = np.append(j, float(test.split()[cen-1]))     # 데이터를 읽어들이면 공백의 difference(차이)를 지니므로 split Function을 이용한다. (기본값은 ' ')
            # 또한, string 형으로 읽어들이므로 실수부 손실이 일어나지 않게끔 float형으로 형 변환을 진행한다. 
            # 우리의 관심사는 Node2_Dsp.out 파일에서는 2열이기 때문에

    return j

# regular expression을 이용해서 parsing을 한 결과 리스트를 반환하는 함수
def glob_re(pattern, strings):
    return list(filter(re.compile(pattern).match, strings))

path = './Term_Project/'        # 기본적으로 Term_Project보다 상위 폴더에 본 코드 파일을 위치시킨다. -> .는 현재 디렉터리이기 때문
parent_list = glob.glob("./Term_Project/Cycle*")    # 앞 글자가 Cycle로 시작하는 디렉터리만 추출
parent_list_len = len(parent_list)      # parent_list의 길이 즉, 앞 글자가 Cycle로 시작하는 디렉터리의 갯수
child_list = []         # ./Term_Project/ 아래의 Cycle로 시작하는 디렉터리들을 저장하기 위한 리스트
child_list_len = []     # 각 Cycle 디렉터리 내에 존재하는 폴더들의 수를 저장하기 위한 리스트

energy_name = []        # 연성 에너지를 엑셀로 추출할 때, 구분을 위해 폴더명을 저장하기 위한 리스트
energy = []             # 연성 에너지를 엑셀로 추출할 때, 그 연성 에너지를 저장하기 위한 리스트

my_name = []            # 항복 모멘트를 엑셀로 추출할 때, 구분을 위해 폴더명을 저장하기 위한 리스트
my = []                 # 항목 모멘트를 엑셀로 추출할 때, 그 항복 모멘트를 저장하기 위한 리스트

for i, j in enumerate(parent_list):             # i에는 parent_list의 인덱스 값이, j에는 element 값이 들어간다.
    child_list.append(glob_re(r'[0-9]*\-[a-zA-Z]*_[a-zA-Z]*', os.listdir(j+'/'))) # regexp를 이용해 각 Cycle 폴더 내의 element와 materials 폴더 제외
    child_list_len.append(len(child_list[i]))       # child_list의 길이 저장


# 마지막 추가 20점 문제 -> 그래프의 항복 모멘트(My) 값을 구하는 문제
# 기본적으로 항복 모멘트를 구하고 그때의 직선을 그래프에 plot한다.
# 이렇게 curvature-moment diagram과 항복 모멘트를 산출할 때의 직선을 plot한 figure을 각각 저장한다.
for i, j in enumerate(parent_list):             # i에는 parent_list의 인덱스 값이, j에는 element 값이 들어간다.
    for k, t in enumerate(child_list[i]):
        two_column = read_file(j+'/'+t+'/'+'PushoverOutput'+'/'+'Node2_Dsp.out', 2)     # Node2_Dsp.out 파일 읽어들임, 2열
        six_column = read_file(j+'/'+t+'/'+'PushoverOutput'+'/'+'Node4_Rection.out', 6)     # Node4_Rection.out 파일 읽어들임, 6열
        six_column = six_column*(-1)*math.pow(10, -6)       # 6열의 값은 실제로 열어보면 -가 붙어있고, 우리가 도출하려는 그래프는 양의 값이기 때문에 -를 취해준다.
        # 또한, 과제에 제시된 그래프의 y에 *10^-6 되어 있으므로 이것도 반영한다. 

        max_moment_index = np.argmax(six_column)        # np.argmax를 이용해서 six_column 즉, 6열에서의 최댓값에 해당하는 인덱스를 저장한다.
        max_moment = np.max(six_column)                 # 그때의 최대 six_column 값도 저장한다.

        energy_name.append(t[t.find('_')+1:])       # 엑셀에 저장하기 위한 연성에너지를 구분하기 위한 폴더명,
        # 과제에 제시된 규칙을 보면 문자 '_' 다음부터 마지막 문자까지 저장하는 것을 확인할 수 있음.
        energy.append(get_area(two_column[0:max_moment_index+1], six_column[0:max_moment_index+1]))     # 0부터 max_moment_index+1까지(max_moment_index를 포함해야 하므로)에
        # 해당하는 즉, 0부터 six_column의 최댓값까지 구간에서의 diagram 아래의 면적을 도출하고 이를 energy 리스트에 추가한다.

        x1 = np.linspace(0, 0.004, num=1000)        # 0.001531과 원점을 지나는 직선의 x
        x2 = np.linspace(0, two_column[max_moment_index]+0.001, num=1000)       # 극한 모멘트를 지나고 우리가 실질적으로 기울기를 조정하면서 직선 아래의 면적과
        # diagram 아래의 면적이 일치하게끔 해야하는 직선의 x

        y_inter = np.interp(0.001531, two_column, six_column)       # 0.001531과 원점을 지나는 직선의 y값을 구하기 위해 우선 x=0.001531에 해당하는 diagram 위의 y 값을 도출한다.

        # 그래야만 기울기를 도출해서 아래와 같이 y에 대한 직선의 식을 구성할 수 있다.

        y1 = (y_inter/0.001531)*x1

        slope = 0       # 극한 모멘트를 지나고 우리가 실질적으로 기울기를 조정하면서 직선 아래의 면적과 diagram 아래의 면적이 일치하게끔 해야하는 직선의

        # 초기 기울기 값은 0으로 설정한다.

        while True:     # 반복의 횟수를 명확히 할 수 없기 때문에 for 대신 while을 사용한다.
        # 또한, 무한 반복문을 구성해준다.
            y2 = slope*(x2-two_column[max_moment_index])+max_moment     # 극한 모멘트를 지나고 우리가 실질적으로 ... 해야하는 직선의 식을 구성해준다.
            
            # 교차점을 구하기 위한 사전작업
            first_line = LineString(np.column_stack((x1, y1)))  # 0.001531과 원점을 지나는 직선          
            second_line = LineString(np.column_stack((x2, y2))) # 극한 모멘트를 지나고 우리가 실질적으로 ... 해야하는 직선
            intersection = first_line.intersection(second_line) # 그 두 직선의 교차점
            
            x_n1 = np.linspace(0, intersection.xy[0][0], num=1000)  # 교차점의 x좌표를 알고 있으나 이 값은 위에서 구성한 numpy array에는 존재하지 않는 값이므로

            # 왜냐하면 수치적으로 더 정밀한 기법을 사용해서 더 정확한 값을 도출했기 때문에 기존에 존재하는 값과는 차이가 발생할 수 밖에 없음.

            # 그러므로 여기서 데이터를 가공하는 것보다는 차라리 얻은 값으로 기존의 직선의 식을 새로 구성해주는 방식을 선택한다.

            # 즉, 0부터 교차점의 x좌표까지를 0.001531과 원점을 지나는 직선을 구성해주고,

            y_n1 = (y_inter/0.001531)*x_n1


            # 교차점의 x좌표부터 diagram의 극한 모멘트의 x좌표까지를 극한 모멘트를 지나고 우리가 실질적으로 ... 해야하는 직선으로 구성해준다.
            x_n2 = np.linspace(intersection.xy[0][0], two_column[max_moment_index])
            y_n2 = slope*(x_n2-two_column[max_moment_index])+max_moment
            

            # 대기 시간이 기므로, 별도로 print 문을 구성하여 계산이 적절하게 이루어지는지 확인하기 위해 구성한 print문들
            # 바로 아래 구문은 diagram의 원점부터 극한 모멘트까지의 면적을 산출한다.
            print(get_area(two_column[0:max_moment_index+1], six_column[0:max_moment_index+1]))

            # 0부터 교차점의 x좌표까지를 0.001531과 원점을 지나는 직선 아래의 면적
            print(get_area(x_n1, y_n1))
            # 교차점의 x좌표부터 diagram의 극한 모멘트의 x좌표까지를 극한 모멘트를 지나고 우리가 실질적으로 ... 해야하는 직선 아래의 면적
            print(get_area(x_n2, y_n2))


            # 정확한 값을 산출하면 좋겠지만, 그러려면 많은 자원(시간, 전깃세, ... 등이 소요되므로) 대략적으로 오차 범위 내에 해당하는
            # 원점부터 극한 모멘트까지의 diagram 아래의 면적과 직선 아래의 면적이 같아지는 그때의 항복모멘트 값을 도출해내고 이를 my list에 추가한다.
            # my_name list는 엑셀에 항복 모멘트를 내보낼 때, 구분을 하기 위한 목적으로 구성된 리스트이고, Cycle 내에 존재하는 21개의 폴더명으로(과제에 제시된 형식 준수) 저장된다.
            if(abs(get_area(two_column[0:max_moment_index+1], six_column[0:max_moment_index+1])-(get_area(x_n1, y_n1) + get_area(x_n2, y_n2))) < 0.01):
                my_name.append(t[t.find('_')+1:])
                my.append(y_n1[-1])
                break

            # 기울기는 500씩 더하면서 즉, 직선을 반시계 방향으로 돌린다.
            slope = slope + 500
        

        # 0.001531과 원점을 지나는 직선을 plot한다.
        plt.plot(x1, y1, 'b--')
        # 극한 모멘트를 지나고 우리가 실질적으로 ... 해야하는 직선을 plot한다.
        plt.plot(x2, y2, 'b--')
        # diagram을 plot한다.
        plt.plot(two_column, six_column, 'k-+', label=t[3:], markersize=5)
        # diagram의 원점부터 극한 모멘트(포함)까지 구간의 아래에 회색을 칠한다.
        plt.fill_between(two_column[0:max_moment_index+1], six_column[0:max_moment_index+1], color='#D0D3D4')
        # x축 레이블 지정
        plt.xlabel('Curvature ϕ [/m]')
        # x축 간격은 0.001이고 0부터 0.010까지(포함 x) 표시
        plt.xticks(np.arange(0, 0.010, 0.001))
        # y축 레이블 지정
        plt.ylabel('Moment [kN·m]')
        # y축 간격은 1000이고 0부터 9000까지(포함 x) 표시
        plt.yticks(np.arange(0, 9000, 1000))
        # y의 최소값은 0 즉, y가 0보다 작은 부분이 표시되는 것을 삭제 처리
        plt.ylim(ymin=0)
        # 범례의 위치는 x=0, y=0.92 위치에 설정
        plt.legend(loc=(0, 0.92))


        # 만약 Figures 폴더가 없다면
        if not os.path.exists(j+'/'+'Figures'):
            os.makedirs(j+'/'+'Figures')        # Figures 폴더를 만든다.


        # 과제의 형식에 맞게끔 각각의 figure를 저장한다.
        plt.savefig(j+'/'+'Figures'+'/'+t[3:]+'.png')
        plt.close()     # 내부 반복문을 돌 때마다 close를 하지 않으면 한꺼번에 plot들이 figure 안에 저장되버린다. (이를 이용하여 폴더안의 데이터들을 한 그래프 안에 모두 그린다.)


    # 연성에너지와 항복모멘트 데이터들을 엑셀로 내보내기 위한 구문들
    e_df = pd.DataFrame({'':energy_name, 'E':energy})
    e_df.to_excel(j+'/'+j[15:].replace('/', '')+'-Energy'+'.xlsx', index=False)
    my_df = pd.DataFrame({'':my_name, 'My':my})
    my_df.to_excel(j+'/'+j[15:].replace('/', '')+'-My'+'.xlsx', index=False)

# 라인 스타일을 dictionary로 지정하여 key에 해당하는 값들을 꺼내기 쉽게 만들어준다.
line_style = {'1':'-', '3':':', '5':'--', '7':'-.', 'none': (0, (3, 1, 1, 1, 1, 1))}

for i, j in enumerate(parent_list):
    for k, t in enumerate(child_list[i]):
        two_column = read_file(j+'/'+t+'/'+'PushoverOutput'+'/'+'Node2_Dsp.out', 2)
        six_column = read_file(j+'/'+t+'/'+'PushoverOutput'+'/'+'Node4_Rection.out', 6)
        six_column = six_column*(-1)*math.pow(10, -6)

        max_moment_index = np.argmax(six_column)
        max_moment = np.max(six_column)

        x1 = np.linspace(0, 0.004, num=1000)
        x2 = np.linspace(0, two_column[max_moment_index]+0.001, num=1000)

        y_inter = np.interp(0.001531, two_column, six_column)

        y1 = (y_inter/0.001531)*x1

        # 별도로 if문을 구성해주지 않고, 만약 마지막 문자가 숫자가 아닌 문자라면 int형 변환시 오류가 일어난다는 점에 착안하여(이러한 Trick을 이용하여) try~catch문으로 구성했다.
        # 00-non_retrofitted의 경우 마지막은 다른 폴더명(element, materials, + Figures 제외)과는 다르게 숫자가 아닌 문자이다.
        try:
            int(t[-1])      # 00-non_retrofitted의 경우 ValueError 발생
            plt.plot(two_column, six_column, label=t[t.find('_')+1:], linestyle=line_style[t[-1]], markersize=0.1)
        except ValueError:
            plt.plot(two_column, six_column, label='none', linestyle=line_style['none'], markersize=0.1)        # 00-non_retrofitted의 경우
        plt.xlabel('Curvature ϕ [/m]')
        plt.xticks(np.arange(0, 0.010, 0.001))
        plt.ylabel('Moment [kN·m]')
        plt.yticks(np.arange(0, 9000, 1000))
        plt.ylim(ymin=0)
        plt.legend(loc=(0.3, 0), ncol=3, prop={'size': 8})

        if not os.path.exists(j+'/'+'Figures'):
            os.makedirs(j+'/'+'Figures')

        # 위에서 상술했듯이 plt를 내부 반복문에서 닫아주지 않는 경우 한꺼번에 plot들이 하나의 figure 안에 들어가므로
        
        plt.savefig(j+'/'+'Figures'+'/'+'all'+'.png')

    plt.close() # 이러한 점에 착안하여 내부 반복문이 끝난 다음 close를 해준다.



        
        

        
