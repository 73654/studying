<template>
    <div class="tables">
        <div class="total">

            <el-row :gutter="30">
                <el-col :span="6">
                    <div class="grid-content ep-bg-purple" />
                    <el-button type="primary"
                        @click="dialogFormVisible = true; Title = '新增用例'; clearData()">新增用例</el-button>
                    <el-button type="success" @click="handleExcute">批量运行</el-button>
                </el-col>
            </el-row>
        </div>


        <el-dialog v-model="dialogFormVisible" :title="Title">
            <el-form :model="form">
                <el-form-item v-if="data == 'edit'" label="用例id">
                    <el-input v-model="form.id" disabled />
                </el-form-item>
                <el-form-item label="名称">
                    <el-input v-model="form.name" autocomplete="off" />
                </el-form-item>
                <el-form-item label="路径">
                    <el-input v-model="form.url" autocomplete="off" />
                </el-form-item>
                <el-form-item label="方法">
                    <el-select v-model="form.method" placeholder="请选择请求方法">
                        <el-option label="GET" value="GET" />
                        <el-option label="POST" value="POST" />
                        <el-option label="PUT" value="PUT" />
                        <el-option label="DELETE" value="DELETE" />
                    </el-select>
                </el-form-item>
                <el-form-item label="参数">
                    <el-input v-model="form.params" autocomplete="off" type="textarea" />
                </el-form-item>
                <el-form-item label="数据">
                    <el-input v-model="form.data" autocomplete="off" type="textarea" />
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


        <!-- 数据表格 -->
        <el-scrollbar height="550px">
            <el-table ref="multipleTableRef" :data="tableData" style="width: 100%"
                @selection-change="handleSelectionChange">
                <el-table-column type="selection" width="55" />
                <el-table-column prop="name" label="用例名称" />
                <el-table-column prop="url" label="请求url" />
                <el-table-column prop="method" label="请求方法" />
                <el-table-column prop="params" label="参数" />
                <el-table-column prop="data" label="数据" />
                <el-table-column label="操作">
                    <template #default="scope">
                        <el-button size="small"
                            @click="dialogFormVisible = true; Title = '修改用例'; handleEdit(scope.$index) ">修改</el-button>
                        <el-button size="small" type="danger" @click="handleDelete(scope.row.id)">删除</el-button>
                        <el-button size="small" type="primary" @click="debug(scope.row.id)">调试</el-button>
                    </template>
                </el-table-column>
            </el-table>
        </el-scrollbar>
    </div>
    <el-text type="success">用例总数：{{ totalNum }}</el-text>
</template>
  
<script setup>
import { ref, computed, onMounted } from "vue";
import { ElMessage, ElMessageBox } from 'element-plus'

const dialogFormVisible = ref(false)
const data = ref('add')

const tableData = ref([])
// 计算用例数量
const totalNum = computed(() => {
    return tableData.value.length
})

// 表单数据
const form = ref({
    id: '',
    name: '',
    url: '',
    method: '',
    params: '',
    data: '',
})
// 提交
const submit = () => {
    if (data.value == "add") {
        $api.testcase
            .addTestcase(form.value)
            .then((result) => {
                if (result.data.code == 0) {
                    ElMessage.success(result.data.msg);
                } else {
                    ElMessage.warning(result.data.msg);
                }
                initData()
            }).catch((err) => {
                ElMessage.error(err);
            })
    }
    if (data.value == "edit") {
        $api.testcase
            .updateTestcase(form.value)
            .then((result) => {
                if (result.data.code == 0) {
                    ElMessage.success(result.data.msg);
                } else {
                    ElMessage.warning(result.data.msg);
                }
                // 修改成功后，调用查询接口，加载表格数据
                initData()
            })
    }
    clearData()
}
// 清空表单操作
const clearData = () => {
    form.value = {
        id: '',
        name: '',
        url: '',
        method: '',
        params: '',
        data: '',
    }
    data.value = "add"
}
// 点击取消重新获取数据
const cancle = () => {
    $api.testcase.getTestcase().then((result) => {
        console.log('result', result)
        tableData.value = result.data.data
    })
}

const handleEdit = (index) => {
    form.value = tableData.value[index]
    data.value = "edit"
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
            $api.testcase
                .deleteTestcase({ id: id })
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
const debug = (id) => {
    $api.testcase
        .debugTestcase({ id: id })
        .then((result) => {
            if (result.data.code == 0) {
                ElMessage.success(result.data.msg);
            } else {
                ElMessage.warning(result.data.msg);
            }
        }).catch((err) => {
            console.log("err", err);
        })
}

// 批量运行

const handleExcute = () => {
    $api.task
        .executeTask({ ids: idList.value })
        .then((result) => {
            if (result.data.code == 0) {
                ElMessage.success("执行成功");
            } else {
                ElMessage.warning(result.data.msg);
            }
        }).catch((err) => {
            console.log("err", err);
        })
}
// id数组
const idList = ref([])

// 勾选后自动触发
const handleSelectionChange = (items) => {
    idList.value = items.map(value => value.id)
}
// 初始化表格数据
const initData = () => {
    $api.testcase
        .getTestcase()
        .then((result) => {
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
  
<style></style>