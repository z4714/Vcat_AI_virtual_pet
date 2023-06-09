---

---

# API设计

## 1.FastApi

## 2.api设计

### 2.1 upload_file

1. POST:http://localhost:1002/api/local_doc_qa/upload_file

2. Body parameter

   1. ```json
      {"file":"file",
      "knowledge_base_id": "string"}
      ```

3. >Example responses

   > 200 Response
	 1. ```json
	    {
	        "code": 200,
	        "msg": "文件 file.md 已上传至新的知识库，并已加载知识库，请开始提问。"
	    }
	    ```

### 2.2list_files

1. GET:http://localhost:1002/api/local_doc_qa/list_files

2. Body parameter

   1. ```json
      {"knowledge_base_id":"string"}
      ```

3. >Example responses
   >
   >200 Response
   >
   1. ```json
      {
          "code": 200,
          "msg": "success",
          "data": [
              "kb1",
              "kb2",
              "kb3"
          ]
      }
      ```
   
      