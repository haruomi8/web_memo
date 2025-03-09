import streamlit as st

st.title("pass_note")
SECRET_PASSWORD = "aaa"

# 合言葉入力
password = st.text_input("enter password", type="password") #type="password"で、隠された入力になる

# 日記の入力と保存
if password == SECRET_PASSWORD:
    st.success("OK")
    st.warning("attention:be use local network.don't deploy this")


    try:
        with open("vault2.txt", "r", encoding="utf-8") as f:
            st.text(f.read())
    except:
        st.warning("text not found")

    entry = st.text_area("write for file:")
    if st.button("save"):
        with open("vault.txt", "a", encoding="utf-8") as f:
            save_string = entry + "\n" + "\n"
            f.write(save_string) #ファイルに書き込む
            st.success("saved")
        st.rerun() #ページを再実行

    if st.button("delete all"):
        with open("vault.txt", "w", encoding="utf-8") as f:
            st.write(" ")
        st.rerun()

elif password > SECRET_PASSWORD:
    st.success("invalid password")
        
else:
    ("enter passcode -> see text")
    ("invaid pascode -> can't see text")