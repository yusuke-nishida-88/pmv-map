# -*- coding: utf-8 -*-
import os
import git

# 実行中のカレントディレクトリをスクリプトがあるディレクトリに固定
os.chdir(os.path.dirname(os.path.abspath(__file__)))

os.system('git add .')
os.system('git commit -m "add data"')
os.system('git push')

#Pushしたいリポジトリに移動
#os.chdir(r'./pmv-map')
#repo = git.Repo()

#最新を取り込むため一旦Pull
#o = repo.remotes.origin
#o.pull()

#add
#repo.git.add('index.html')

#Commit(サブディレクトリ含めて全て)
#repo.git.commit('index.html', message='new file', author='yusuke.nishida@woven-planet.global')

#Push
#repo.git.push('origin', 'new_branch')
#origin = repo.remote(name='origin')
#origin.push()