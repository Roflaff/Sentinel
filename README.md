# Sentinel

> **Sentinel**은 시스템 리소스와 에이전트 동작을 **Grafana 기반 대시보드**로 실시간 모니터링하는 플랫폼입니다.  
Prometheus와 다양한 Exporter(Node, GPU, Langfuse)를 통해 수집한 메트릭을 Grafana에서 한눈에 확인할 수 있습니다.

---

## 📊 아키텍처

<p align="center">
  <img src="./docs/architecture.png" alt="Sentinel Architecture" width="600"/>
</p>

---

## 🚀 주요 기능
- **Langfuse 연동**: LLM/에이전트 이벤트 및 실행 로그 추적
- **시스템 리소스 모니터링**
  - CPU, 메모리, 디스크, 네트워크 상태 (Node Exporter)  
  - GPU 사용량 (DCGM Exporter)  
  - LLM 실행 메트릭 (Langfuse Exporter)
- **Grafana 대시보드**: 실시간 시각화 및 모니터링
- **알림 기능 (추가 예정)**: 임계치 초과 시 Slack / Email / Webhook 알림
