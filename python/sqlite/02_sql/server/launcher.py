import network
import uvicorn


if __name__ == '__main__':
    print(f"Server running on http://{network.get_host_ip()}:{network.port}")
    uvicorn.run(
        "app:app",
        host='0000',
        port=network.port,
        reload=True
    )
    
