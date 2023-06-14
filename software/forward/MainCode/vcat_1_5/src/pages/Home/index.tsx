import React,{useEffect,useState} from 'react';
import { PageContainer } from '@ant-design/pro-components';
import { useModel } from '@umijs/max';
import { trim } from '@/utils/format';
import Guide from '@/components/Guide';
import { Widget } from 'react-chat-widget';
import 'react-chat-widget/lib/styles.css';
import styles from './index.less';
import { chat } from '@/api';
import { InitialStateType, UserInfo, LoginResponse, getInitialState } from '@/app';



const HomePage: React.FC = () => {
  const { name } = useModel('global');
  const { initialState, setInitialState } = useModel('@@initialState');
  const [updatedInitialState, setUpdatedInitialState] = useState(initialState);
  const [chatHistory, setChatHistory] = useState<[]>([]);
  const [chatResponse, setChatResponse] = useState('');
 

  useEffect(() => {
      setUpdatedInitialState(initialState);
    }, [initialState]);

    const init = updatedInitialState as InitialStateType;
    const cat_name = init.cat_name;
 
    const handleNewUserMessage = async (newMessage: string) => {
      try {
        console.log(newMessage);
        const response = await chat(newMessage, chatHistory);
        console.log(response);
        setChatResponse(response.response);
        setChatHistory(response.history);
      } catch (error) {
        console.error(error);
      }
    };





  
  return (
    <PageContainer ghost>
      <div className={styles.container}>
        <Guide name={trim(name)} />
        <div className={styles.chatContainer}>
          <Widget
            handleNewUserMessage={handleNewUserMessage}
            title="Chat with your Vcat~"
            subtitle={`当前宠物: ${cat_name}`}
          />
          <div className={styles.chatResponse}>{chatResponse}</div>
        </div>
      </div>
    </PageContainer>
  );
};

export default HomePage;
