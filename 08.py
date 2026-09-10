# 第八题: 校园摄影比赛作品管理
# 请补全类实现, 不要修改类名和方法名.

class WorkError(Exception):
    # 作品属性或操作非法时抛出的异常
    pass

# 基类 Work: 属性 title, author, likes, rating
#   - title 不能为空字符串
#   - author 不能为空字符串
#   - likes 不能小于 0
#   - rating 初始为 0
#   - like(): 点赞数 +1
#   - score(value): 给作品打分, value 必须在 0 到 10 之间
#   - rename(new_title): 修改作品名, new_title 不能为空字符串
#   - __str__(): 输出类型, 作品名, 作者, 点赞数和评分
class Work:
    def __init__(self, title, author, likes):
        # --------------在下面完成代码--------------------
        pass

    def like(self):
        # --------------在下面完成代码--------------------
        pass

    def score(self, value):
        # --------------在下面完成代码--------------------
        pass

    def rename(self, new_title):
        # --------------在下面完成代码--------------------
        pass

    def __str__(self):
        # --------------在下面完成代码--------------------
        pass

# 子类 PhotoWork(Work): 图片作品
#   - 使用 super().__init__() 初始化父类属性
#   - 额外属性 resolution, 不能为空字符串
#   - 类型设置为 图片作品
#   - 重写 like(): 点赞数 +2
#   - 重写 __str__(): 在父类信息后追加分辨率
class PhotoWork(Work):
    def __init__(self, title, author, likes, resolution):
        # --------------在下面完成代码--------------------
        pass

    def like(self):
        # --------------在下面完成代码--------------------
        pass

    def __str__(self):
        # --------------在下面完成代码--------------------
        pass

# 子类 VideoWork(Work): 视频作品
#   - 使用 super().__init__() 初始化父类属性
#   - 额外属性 duration, 必须大于 0
#   - 类型设置为 视频作品
#   - 重写 like(): 点赞数 +3
#   - 重写 __str__(): 在父类信息后追加时长
class VideoWork(Work):
    def __init__(self, title, author, likes, duration):
        # --------------在下面完成代码--------------------
        pass

    def like(self):
        # --------------在下面完成代码--------------------
        pass

    def __str__(self):
        # --------------在下面完成代码--------------------
        pass

if __name__ == "__main__":
    work = None
    while True:
        print("1. 创建作品")
        print("2. 查看作品")
        print("3. 点赞")
        print("4. 打分")
        print("5. 重命名")
        print("q. 退出")
        choice = input().strip()

        if choice == "q":
            break

        if choice == "1":
            kind = input().strip()
            title = input().strip()
            author = input().strip()
            try:
                likes = int(input().strip())
                if kind == "1":
                    resolution = input().strip()
                    work = PhotoWork(title, author, likes, resolution)
                elif kind == "2":
                    duration = float(input().strip())
                    work = VideoWork(title, author, likes, duration)
                else:
                    print("错误: 类型必须是 1 或 2")
                    continue
                print(f"创建成功! {work}")
            except WorkError as e:
                print(f"错误: {e}")
            except ValueError:
                print("错误: 点赞数必须是整数, 时长必须是数字")
        elif choice == "2":
            if work is None:
                print("错误: 请先创建作品")
            else:
                print(work)
        elif choice == "3":
            if work is None:
                print("错误: 请先创建作品")
            else:
                work.like()
        elif choice == "4":
            if work is None:
                print("错误: 请先创建作品")
            else:
                try:
                    value = float(input().strip())
                    work.score(value)
                except WorkError as e:
                    print(f"错误: {e}")
                except ValueError:
                    print("错误: 评分必须是数字")
        elif choice == "5":
            if work is None:
                print("错误: 请先创建作品")
            else:
                new_title = input().strip()
                try:
                    work.rename(new_title)
                except WorkError as e:
                    print(f"错误: {e}")
        else:
            print("错误: 请输入 1, 2, 3, 4, 5 或 q")
