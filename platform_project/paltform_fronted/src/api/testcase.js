import API from './http'

const testcase = {
    // 查询接口
    getTestcase() {
        return API({
            // 请求方法
            method: 'GET',
            // 请求路由
            url: 'testcase/list',
        })
    },

    // 新增
    addTestcase(data) {
        return API({
            // 请求方法
            method: 'POST',
            // 请求路由
            url: 'testcase/add',
            // 请求数据
            data: data
        })
    },

    // 修改
    updateTestcase(data) {
        return API({
            // 请求方法
            method: 'POST',
            // 请求路由
            url: 'testcase/update',
            // 请求数据
            data: data
        })
    },

    // 删除
    deleteTestcase(params) {
        return API({
            // 请求方法
            method: 'POST',
            // 请求路由
            url: 'testcase/delete',
            // 请求数据
            params: params
        })
    },

    // 调试
    debugTestcase(params) {
        return API({
            // 请求方法
            method: 'POST',
            // 请求路由
            url: 'testcase/debug',
            // 请求数据
            params: params
        })
    },
}

export default testcase
