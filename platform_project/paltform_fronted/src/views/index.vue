
<template>
  <el-container>
    <!-- 顶部栏 -->
    <el-header style="text-align: center; font-size: 30px;border-bottom: 2px;">
      <div style="display: flex;justify-content: center;align-items: center;">
        <el-icon :size="40" class="is-loading">
          <ChromeFilled />
        </el-icon>
        <p>🐂🐦测试平台</p>
        <el-icon :size="40" class="is-loading">
          <ChromeFilled />
        </el-icon>
      </div>
    </el-header>
    <el-container>
      <el-aside width="150px">
        <el-menu background-color="Transparent" text-color="#000000" active-text-color="#409eff">
          <el-menu-item index="1" @click="goTo('/index/testcase')">
            <el-icon :size="40">
              <setting />
            </el-icon>
            测试用例
          </el-menu-item>
          <el-menu-item index="2" @click="goTo('/index/task')">
            <el-icon :size="40">
              <setting />
            </el-icon>
            测试任务
          </el-menu-item>
        </el-menu>
      </el-aside>
      <el-main>
        <router-view></router-view>
      </el-main>
    </el-container>
  </el-container>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { Setting } from '@element-plus/icons-vue'
const router = useRouter()

const goTo = (path) => {
  router.push(path)
}
</script>

<style scoped>
.el-container {
  height: 100%;
}

.el-header {
  padding: 0;
}

.el-aside>ul {
  height: 100%;
}

.flex-grow {
  flex-grow: 1;
}

.el-main {
  overflow: hidden;
}
</style>