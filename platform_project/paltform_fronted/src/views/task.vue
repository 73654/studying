<template>
    <div class="tables">
        <div class="total">
            <el-row :gutter="30">
                <el-col :span="6">
                    <div class="grid-content ep-bg-purple" />
                    <el-button type="primary"
                        @click="dialogFormVisible = true; Title = '新增用例'; clearData()">新增任务</el-button>
                    <el-button type="danger" @click="handleExcute">批量删除</el-button>
                </el-col>
            </el-row>
        </div>
        <el-scrollbar height="550px">
            <el-table ref="multipleTableRef" :data="tableData" style="width: 100%"
                @selection-change="handleSelectionChange">
                <el-table-column type="selection" width="55" />
                <el-table-column prop="id" label="id编号" />
                <el-table-column prop="name" label="名称" />
                <el-table-column prop="success" label="成功数" />
                <el-table-column prop="total" label="总数" />
                <el-table-column prop="rate" label="成功率" />
                <el-table-column label="操作">
                    <template #default="scope">
                        <el-button size="small" type="danger" @click="handleDelete(scope.row.id)">删除</el-button>
                    </template>
                </el-table-column>
            </el-table>
        </el-scrollbar>
        <el-dialog v-model="dialogFormVisible" :title="Title">
            <el-form :model="form">
                <el-form-item label="名称">
                    <el-input v-model="form.name" autocomplete="off" />
                </el-form-item>
                <el-form-item label="成功数">
                    <el-input v-model="form.success" autocomplete="off" />
                </el-form-item>
                <el-form-item label="总数">
                    <el-input v-model="form.total" autocomplete="off" />
                </el-form-item>
                <el-form-item label="成功率">
                    <el-input v-model="form.rate" autocomplete="off" />
                </el-form-item>
            </el-form>
            <template #footer>
                <span class="dialog-footer">
                    <el-button @click="dialogFormVisible = false; cancle()">取消</el-button>
                    <el-button type="primary" @click="dialogFormVisible = false; submit()">
                        确定
                    </el-button>
                </span>
            </template>
        </el-dialog>
        <el-text type="success">任务总数：{{ totalNum }}</el-text>
    </div>
</template>
  
<script setup>
import { ref, computed, onMounted } from "vue";
import { ElMessage, ElMessageBox } from 'element-plus'
const tableData = ref([]);
const dialogFormVisible = ref(false)
// 计算任务数量
const totalNum = computed(() => {
    return tableData.value.length
})

const handleExcute = () => {
    ElMessage.error("好不容易添加的,不许批量删");
}
// 表单数据
const form = ref({
    name: '',
    success: '',
    total: '',
    rate: '',
})

const submit = () => {
    $api.task
        .addTask(form.value)
        .then((result) => {
            if (result.data.code == 0) {
                ElMessage.success(result.data.msg);
                tableData.value = result.data.data
            } else {
                ElMessage.warning(result.data.msg);
            }
            initData()
        }).catch((err) => {
            console.log("err", err);
        })
}

// 清空表单操作
const clearData = () => {
    form.value = {
        name: '',
        success: '',
        total: '',
        rate: '',
    }
}
const handleDelete = (id) => {
    ElMessageBox.confirm(
        '确定删除？删除后数据将无法找回',
        '警告',
        {
            confirmButtonText: '确定',
            cancelButtonText: '取消',
            type: 'warning',
        }
    )
        .then(() => {
            // 删除用例
            // 调用删除接口
            $api.task
                .deleteTask({ id: id })
                .then((result) => {
                    if (result.data.code == 0) {
                        ElMessage.success(result.data.msg);
                    } else {
                        ElMessage.warning(result.data.msg);
                    }
                    // 删除成功后，调用查询接口，加载表格数据
                    initData()
                })
        })
        .catch(() => {
            ElMessage.info('取消删除')
        })
}

// 初始化表格数据
const initData = () => {
    $api.task
        .getTask()
        .then((result) => {
            console.log('result', result.data);
            if (result.data.code == 0) {
                ElMessage.success(result.data.msg);
                tableData.value = result.data.data
            } else {
                ElMessage.warning(result.data.msg);
            }
        }).catch((err) => {
            console.log("err", err);
        })
}

onMounted(() => {
    initData()
})
</script>