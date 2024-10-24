import streamlit as st


def message() -> str:
    """ Simple String Message """
    return 'Running Container.'


def main() -> None:
    """ Simple Application Entry Point """
    st.write(message())


if __name__ == '__main__':
    main()
