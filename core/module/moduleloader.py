# coding=utf-8
# @Author   : zpchcbd HG team
# @Time     : 2021-09-07 16:47

import importlib
import os
import re
from core.constant import ModulePath
from core.variablemanager import GlobalVariableManager


# import sys
abs_path = os.getcwd() + os.path.sep  # 路径


# 模块加载类，用于加载poc用的，相当于一个模块Manager，写这个是用到后面出现新POC检测配合fofa来进行使用，这样会比较方便处理
# exp loader, study for python
class ModuleLoader(object):
    def __init__(self, moduleType):
        self.moduleList = []

    def moduleLoad(self, moduleType, moduleObject=None):
        try:
            if moduleObject is None:
                return self._defaultModuleLoad(moduleType=moduleType)  # moduleType: third | exploit
            elif isinstance(moduleObject, str):
                return self._singleModuleLoad(
                    module=moduleObject)  # single module load, for example exploit.web.v2Conference.sql_inject
            elif isinstance(moduleObject, list):
                return self._multiModuleLoad(
                    moduleList=moduleObject)  # multi module load, for example exploit.web.v2Conference.sql_inject,
        except ModuleNotFoundError as e:
            print('module not found, {}'.format(e.__str__()))
            return None

    # 后面的用于单个payload检测，要不然每次都需要写个py文件来跑，太麻烦
    # for single 单个测试
    def _singleModuleLoad(self, module: str):
        try:
            modulePY = importlib.import_module(module)
            if hasattr(modulePY, 'Script'):
                aModule = getattr(modulePY, 'Script')
                self.moduleList.append(aModule)
        except Exception as e:
            print('import module {} error, {}'.format(module, e.__str__()))
        return self.moduleList

    # for twp/three poc exp 加载>2
    def _multiModuleLoad(self, moduleList: list):
        for module in moduleList:
            try:
                modulePY = importlib.import_module(module)
                if hasattr(modulePY, 'Script'):
                    aModule = getattr(modulePY, 'Script')
                    self.moduleList.append(aModule)
            except Exception as e:
                print('import module {} error, {}'.format(module, e.__str__()))
        return self.moduleList

    # default, all module 加载所有的
    def _defaultModuleLoad(self, moduleType):
        # default
        # 因为分目录了，所以这里想要动态加载模块只能是os.walk()
        # sys.path.append(self.modulePath)

        # version: 2
        if moduleType == 'exploit':
            for parent, dirnames, filenameList in os.walk(abs_path + ModulePath.EXPLOIT, followlinks=True):
                dirFileLength = 0
                sameTypeModuleList = []
                for filename in filenameList:
                    if filename[-3:] == 'pyc' or filename[:2] == '__' or filename[-5:] == '__.py' or filename[-3:] != '.py':
                        continue
                    try:
                        filePath = os.path.join(parent, filename)
                        modulePY = importlib.import_module('.'.join(re.split('[\\\\/]', filePath[len(abs_path):-3])))
                        if hasattr(modulePY, 'Script'):
                            # 一般一个同类型的模块只加载一次，那么如果目录文件>=1的话，那么则该目录为同类型多模块
                            if dirFileLength >= 1:
                                aModule = getattr(modulePY, 'Script')
                                sameTypeModuleList.append(aModule)
                            # 不是同类型多模块的处理
                            else:
                                aModule = getattr(modulePY, 'Script')
                                self.moduleList.append(aModule)
                            dirFileLength += 1
                    except Exception as e:
                        print('import module {} error, {}'.format(filename, e.__str__()))
                if sameTypeModuleList:
                    # 如果是同类型多模块的话，那么就存储到全局变量表中，key为当前模块名，值为相关域名的信息和最后要加载的模块对象
                    dirName = re.split('[\\\\/]', parent)[-1]
                    """
                    格式为 
                    [
                        {"seeyon": {"domain": [], "module": [module1(), module2(), module3()]}},
                        {"seeyon": {"domain": [], "module": [module1(), module2(), module3()]}},                    
                    ]
                    """
                    currentModuleList = GlobalVariableManager.getValue("remainModuleList")
                    currentModuleList.append({'name': dirName, 'domain': [], 'module': sameTypeModuleList})
        elif moduleType == 'third':
            for parent, dirnames, filenameList in os.walk(abs_path + ModulePath.THIRDLIB, followlinks=True):
                for filename in filenameList:
                    if filename[-3:] == 'pyc' or filename[:2] == '__' or filename[-5:] == '__.py' or filename[-3:] != '.py':
                        continue
                    try:
                        filePath = os.path.join(parent, filename)
                        modulePY = importlib.import_module(
                            '.'.join(re.split('[\\\\/]', filePath[len(abs_path):-3])))
                        # module = importlib.import_module('FineReport')
                        if hasattr(modulePY, 'do'):
                            aModule = getattr(modulePY, 'do')
                            self.moduleList.append(aModule)
                    except Exception as e:
                        print('import module {} error, {}'.format(filename, e.__str__()))


        # version: 1
        # if moduleType == 'third':
        #     for parent, dirnames, filenameList in os.walk(abs_path + ModulePath.THIRDLIB, followlinks=True):
        #         for filename in filenameList:
        #             if filename[-3:] == 'pyc' or filename[:2] == '__' or filename[-5:] == '__.py' or filename[
        #                                                                                              -3:] != '.py':
        #                 continue
        #             try:
        #                 filePath = os.path.join(parent, filename)
        #                 modulePY = importlib.import_module(
        #                     '.'.join(re.split('[\\\\/]', filePath[len(abs_path):-3])))
        #                 # module = importlib.import_module('FineReport')
        #                 if hasattr(modulePY, 'do'):
        #                     aModule = getattr(modulePY, 'do')
        #                     self.moduleList.append(aModule)
        #             except Exception as e:
        #                 print('import module {} error, {}'.format(filename, e.__str__()))
        # elif moduleType == 'exploit':
        #     for parent, dirnames, filenameList in os.walk(abs_path + ModulePath.EXPLOIT, followlinks=True):
        #         for filename in filenameList:
        #             if filename[-3:] == 'pyc' or filename[:2] == '__' or filename[-5:] == '__.py' or filename[
        #                                                                                              -3:] != '.py':
        #                 continue
        #             try:
        #                 filePath = os.path.join(parent, filename)
        #                 modulePY = importlib.import_module(
        #                     '.'.join(re.split('[\\\\/]', filePath[len(abs_path):-3])))
        #                 # module = importlib.import_module('FineReport')
        #                 if hasattr(modulePY, 'Script'):
        #                     aModule = getattr(modulePY, 'Script')
        #                     self.moduleList.append(aModule)
        #             except Exception as e:
        #                 print('import module {} error, {}'.format(filename, e.__str__()))



        # modules = filter(lambda x: (True, False)[x[-3:] == 'pyc' or x[-5:] == '__.py' or x[:2] == '__'],
        #                  os.listdir(self.modulePath))
        # for _ in modules:
        #     print(_)
        #     module = importlib.import_module(_[:-3])
        #     if hasattr(module, 'Script'):
        #         aClass = getattr(module, self.object)
        #         print(aClass)
        return self.moduleList


if __name__ == '__main__':
    moduleloader = ModuleLoader()
    moduleloader.moduleLoad(moduleType='exploit', module='*')
