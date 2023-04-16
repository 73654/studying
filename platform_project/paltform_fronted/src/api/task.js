import API from './http'

const task = {
    // 查询接口
    getTask() {
        return API({
            // 请求方法
            method: 'GET',
            // 请求路由
            url: 'task/list',
        })
    },
    deleteTask(params) {
        return API({
            // 请求方法
            method: 'POST',
            // 请求路由
            url: 'task/delete',
            // 请求数据
            params: params
        })
    },

    // 新增
    addTask(data) {
        return API({
            // 请求方法
            method: 'POST',
            // 请求路由
            url: 'task/add',
            // 请求数据
            data: data
        })
    },

    // 批量运行
    executeTask(data) {
        return API({
            // 请求方法
            method: 'POST',
            // 请求路由
            url: 'task/execute',
            // 请求数据
            data: data
        })
    },
}

export default task