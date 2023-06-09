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

### 2.3chat

1. POST:http://localhost:1002/api/chat

2. Body parameter

   1. ```json
      {"question": "pisa", "history": []}
      ```

3. >Example responses
   >
   >200 Response
   >
   1. ```json
      {
          "question": "pisa",
          "response": "PISA stands for Performance in International Schools, a standardized test that measures students' knowledge and skills in 10 subjects, including reading, writing, mathematics, and science. The test is administered by the International Society for Testing and Assessment (ISAT) and is used by governments, educational institutions, and organizations to assess the academic performance of students around the world.\n\nPISA measures students' performance in reading, writing, mathematics, and science, and is designed to assess how well students are able to understand and apply the knowledge they are learning. The test is administered in three rounds, with the first round taking place in 2003, the second round in 2007, and the third round in 2010. The test results are used to compare the academic performance of students in different countries and to identify areas where students may need additional support.\n\nPISA is widely recognized as a valuable tool for measuring the academic performance of students and for identifying areas where additional support may be needed. It is used by governments, educational institutions, and organizations to improve educational outcomes and to promote international cooperation and exchange.",
          "history": [
              [
                  "pisa",
                  "PISA stands for Performance in International Schools, a standardized test that measures students' knowledge and skills in 10 subjects, including reading, writing, mathematics, and science. The test is administered by the International Society for Testing and Assessment (ISAT) and is used by governments, educational institutions, and organizations to assess the academic performance of students around the world.\n\nPISA measures students' performance in reading, writing, mathematics, and science, and is designed to assess how well students are able to understand and apply the knowledge they are learning. The test is administered in three rounds, with the first round taking place in 2003, the second round in 2007, and the third round in 2010. The test results are used to compare the academic performance of students in different countries and to identify areas where students may need additional support.\n\nPISA is widely recognized as a valuable tool for measuring the academic performance of students and for identifying areas where additional support may be needed. It is used by governments, educational institutions, and organizations to improve educational outcomes and to promote international cooperation and exchange."
              ]
          ],
          "source_documents": []
      }
      ```
### 2.4BaseResponse

1. POST:http://localhost:1002/api/local_doc_qa/list_files

2. Body parameter

   1. ```json
      {"knowledge_base_id":"string"}
      ```

3. >Example responses
   >
   >200 Response
   1. ```json
       {
          "code": 200,
          "msg": "success",
             }
      ```
### 2.5list_files

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
