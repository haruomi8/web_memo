import streamlit as st

st.title("memo")
st.info("use for todo, memo, other...")

try:
        with open("vault.txt", "r", encoding="utf-8") as f:
            st.write(f.read())
except:
        st.warning("text not found")

entry = st.text_area("write for file:")
if st.button("save"):
        with open("memo.txt", "a", encoding="utf-8") as f:
            save_string = entry + "\n" + "\n"
            f.write(save_string) #ファイルに書き込む
            st.success("saved")
        st.rerun() #ページを再実行

if st.button("delete all"):
        with open("vault.txt", "w", encoding="utf-8") as f:
            st.write(" ")
        st.rerun()