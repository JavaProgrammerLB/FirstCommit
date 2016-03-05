def main():
    own = input('Enter the own of the project:')
    projectName = input('Enter the project name:')
    branch = input('Enter the branch name:')
    num = input('Enter the commit number of {}:'.format(branch))
    result = calculate(int(num))
    print('https://github.com/{}/{}/commits/{}?page={}'.format(own,projectName,branch,str(result)))

def calculate(num):
    result = int(num / 35)
    if num % 35 == 0:
        pass
    else:
        result += 1
    return result

if __name__ == '__main__':
    main()
