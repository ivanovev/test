

def TEST_mntr1():
    TEST_mntr1.val += 1
    if TEST_mntr1.val >= 10:
        TEST_mntr1.val = 0
    return '%d' % TEST_mntr1.val
TEST_mntr1.val = 0

def TEST_ctrl1(v=''):
    if v:
        TEST_ctrl1.val = v
    return TEST_ctrl1.val
TEST_ctrl1.val = '0'

