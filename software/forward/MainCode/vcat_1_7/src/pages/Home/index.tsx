import React,{useEffect,useState,useMemo} from 'react';
import { PageContainer } from '@ant-design/pro-components';
import{Button, notification, Space, Avatar} from 'antd'
import type { NotificationPlacement } from 'antd/es/notification/interface';
import { useModel } from '@umijs/max';
import { trim } from '@/utils/format';
import Guide from '@/components/Guide';
import { Widget } from 'react-chat-widget';
import 'react-chat-widget/lib/styles.css';
import styles from './index.less';
import cx from 'classnames';
import { chat } from '@/api';
import { InitialStateType, UserInfo, LoginResponse, getInitialState } from '@/app';



const HomePage: React.FC = () => {
  const { name } = useModel('global');
  const { initialState, setInitialState } = useModel('@@initialState');
  const [updatedInitialState, setUpdatedInitialState] = useState(initialState);
  const [chatHistory, setChatHistory] = useState<[]>([]);
  const [chatResponse, setChatResponse] = useState('');
  const [noti, contextHolder] = notification.useNotification();
  
  const Context = React.createContext({name:initialState?.name});
  let greet = initialState?.loggedIn ? 'Hello,' : '';
  
  const openNotification = (placement: NotificationPlacement) => {
    noti.info({
      message: `Notification ${placement}`,
      description: <Context.Consumer>{({ name }) => `${greet}${name}`}</Context.Consumer>,
      placement,
    });
  };//注：虽然这样在钩子函数内外各写一个很不优雅，但由于它现在能用，且出现了一个类似于overlap的效果，所以暂不修正
  
  const contextValue = useMemo(() => ({ name: initialState?.name }), []);

  useEffect(() => {
      setUpdatedInitialState(initialState);
  }, [initialState]);

  useEffect(() => {
    
    const openNotification = (placement: NotificationPlacement) => {
      noti.info({
        message: `User Notification`,
        description: (
          <Context.Consumer>{({ name }) => `${greet}${initialState?.name}!`}</Context.Consumer>
        ),
        placement,
      });
    };
    
    if (!initialState?.loggedIn) {
      greet = '请先登录，现在为试用版';
    } else {
      greet = initialState?.loggedIn ? 'Hello,' : '';
    }

    const handleClick = () => {
      openNotification('topLeft');
    };

    const widgetElement = document.querySelector('.rcw-launcher');
    if (widgetElement) {
      widgetElement.addEventListener('click', handleClick);
    }

    return () => {
      if (widgetElement) {
        widgetElement.removeEventListener('click', handleClick);
      }
    };
  }, [initialState?.loggedIn, noti]);

  const init = updatedInitialState as InitialStateType;
  const cat_name = init.cat_name;
 
  const handleNewUserMessage = async (newMessage: string) => {
    try {
      console.log(newMessage);
        const response = await chat(newMessage, chatHistory);
        console.log(response);
        setChatResponse(response.response);
        //test
        //setChatResponse("test");
        setChatHistory(response.history);
      } catch (error) {
        console.error(error);
      }
    };
  
    if (!initialState?.loggedIn) {
      greet = '请先登录,现在为试用版';
      return (
        <PageContainer ghost>
          <div className={styles.container}>
            <Context.Provider value={contextValue}>
              {contextHolder}
            
              <Guide name={trim(name)} />
                <div className={styles.chatContainer}>
                  <Widget
                    handleNewUserMessage={handleNewUserMessage}
                    title="Try Vcat~"
                    subtitle={`当前宠物: Vcat_0`}
                    onClick={() => openNotification('topLeft')}
                  />
                  <div className={styles.chatResponse}>
                    <div className={cx(styles.chatBubble, styles.replyBubble)}>
                      <Avatar src={initialState?.avatar} alt="User:"/>:
                      <div className={styles.bubbleContent}>{chatResponse}</div>
                    </div>
                  </div>
                </div>
              </Context.Provider>
            </div>
          </PageContainer>


      );
    }
  

  greet = initialState?.loggedIn ? 'Hello,' : '';
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
          <div className={styles.chatResponse}>
            <div className={cx(styles.chatBubble, styles.replyBubble)}>
              <div className={styles.bubbleContent}>{chatResponse}</div>
            </div>
          </div>
        </div>
      </div>
    </PageContainer>
  );
};

export default HomePage;
